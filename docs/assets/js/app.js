document.addEventListener('DOMContentLoaded', () => {
    const contentDiv = document.getElementById('content');
    const tocNav = document.getElementById('toc');
    const sidebar = document.getElementById('sidebar');
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const body = document.body;

    // Mobile Sidebar Toggle
    sidebarToggle.addEventListener('click', () => {
        sidebar.classList.toggle('active');
        body.classList.toggle('sidebar-active');
    });

    // Close sidebar when clicking outside on mobile
    document.getElementById('main-content').addEventListener('click', () => {
        if (sidebar.classList.contains('active')) {
            sidebar.classList.remove('active');
            body.classList.remove('sidebar-active');
        }
    });

    // Configure Marked.js
    marked.setOptions({
        gfm: true,
        breaks: true,
        headerIds: true,
        mangle: false,
        sanitize: false // allow HTML for the home page
    });

    // Handle Link Interception
    const interceptLinks = (container) => {
        const links = container.querySelectorAll('a');
        links.forEach(link => {
            const href = link.getAttribute('href');
            // Check if internal markdown link
            if (href && (href.endsWith('.md') || href.endsWith('.html')) && !href.startsWith('http')) {
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    // Convert standard links to hash links
                    let newHash = href;
                    
                    // Clean up relative paths
                    if (newHash.startsWith('./')) {
                        newHash = newHash.substring(2);
                    } else if (newHash.startsWith('../')) {
                        // Very simple parent dir resolution, assuming we are in a subfolder like 'chapters/'
                        newHash = newHash.substring(3);
                    }

                    // Convert .html back to .md for SPA routing since we fetch .md files
                    if (newHash.endsWith('.html')) {
                        newHash = newHash.substring(0, newHash.length - 5) + '.md';
                    }

                    window.location.hash = '/' + newHash;
                });
            }
        });
    };

    // Render TOC from SUMMARY.md
    const loadTOC = async () => {
        try {
            const response = await fetch('./SUMMARY.md');
            if (response.ok) {
                const text = await response.text();
                // Strip the top level heading
                const cleanedText = text.replace(/^# Summary\s+/i, '');
                tocNav.innerHTML = marked.parse(cleanedText);
                interceptLinks(tocNav);
                updateActiveTOC();
            }
        } catch (error) {
            console.error('Failed to load SUMMARY.md:', error);
            tocNav.innerHTML = '<p style="padding:1rem;">無法載入目錄</p>';
        }
    };

    // Update active link in TOC
    const updateActiveTOC = () => {
        const currentHash = window.location.hash || '#/home.md';
        const links = tocNav.querySelectorAll('a');
        links.forEach(link => {
            link.classList.remove('active');
            // Create a fake URL to easily parse the href target
            const targetHref = link.getAttribute('href');
            if(!targetHref) return;
            
            let cleanTarget = targetHref.replace(/^\.\//, '').replace(/^\.\.\//, '');
            if(cleanTarget.endsWith('.html')) cleanTarget = cleanTarget.replace(/\.html$/, '.md');
            
            if (currentHash.includes(cleanTarget)) {
                link.classList.add('active');
            }
        });
    };

    // Load Markdown Content
    const loadContent = async (path) => {
        // Strip leading slash
        let fetchPath = path.startsWith('/') ? path.substring(1) : path;
        
        // Convert home.md request to actually fetch home.md
        if (fetchPath === '' || fetchPath === '/') {
            fetchPath = 'home.md';
        }

        contentDiv.classList.remove('fade-in');
        // Force reflow
        void contentDiv.offsetWidth;

        try {
            const response = await fetch('./' + fetchPath);
            if (response.ok) {
                let text = await response.text();
                // Strip YAML frontmatter
                if (text.startsWith('---')) {
                    const parts = text.split('---');
                    if (parts.length >= 3) {
                        text = parts.slice(2).join('---').trim();
                    }
                }
                contentDiv.innerHTML = marked.parse(text);
                interceptLinks(contentDiv);
                contentDiv.classList.add('fade-in');
                window.scrollTo(0, 0);
            } else {
                contentDiv.innerHTML = `<div class="section-card" style="text-align:center"><h2>404</h2><p>找不到內容 (${fetchPath})</p><a href="#/home.md" class="button-primary" style="margin-top:20px;display:inline-block">返回首頁</a></div>`;
                contentDiv.classList.add('fade-in');
            }
        } catch (error) {
            console.error('Failed to load content:', error);
            contentDiv.innerHTML = `<div class="section-card"><h2>Error</h2><p>載入內容時發生錯誤。</p></div>`;
        }
    };

    // Route handling
    const router = () => {
        let hash = window.location.hash.substring(1); // remove #
        if (!hash) {
            hash = '/home.md';
            window.location.hash = hash;
            return; // hashchange will trigger router again
        }
        loadContent(hash);
        updateActiveTOC();

        // Close mobile sidebar on navigation
        if (sidebar.classList.contains('active')) {
            sidebar.classList.remove('active');
            body.classList.remove('sidebar-active');
        }
    };

    // Initialize
    window.addEventListener('hashchange', router);
    loadTOC().then(() => {
        router();
    });
});
