# 《2026 資安大轉折：AI 時代的網路防禦新規則》

> 一部面向 AI 原生時代的資安趨勢著作，聚焦雲端原生防禦、零信任、AI 攻擊面、供應鏈風險與治理責任。

![GitHub Pages Ready](https://img.shields.io/badge/GitHub%20Pages-ready-0A7B83)
![Markdown](https://img.shields.io/badge/Format-Markdown-1F6FEB)
![Language](https://img.shields.io/badge/Language-zh--TW-B35C00)
![Status](https://img.shields.io/badge/Status-release%20preview-6B7280)

## 目錄

- [封面區塊](#封面區塊)
- [專案說明](#專案說明)
- [內容概覽](#內容概覽)
- [章節導覽](#章節導覽)
- [線上閱讀結構](#線上閱讀結構)
- [補充資源](#補充資源)
- [部署說明](#部署說明)
- [網站結構](#網站結構)

## 封面區塊

**書名**

2026 資安大轉折：AI 時代的網路防禦新規則

**副標**

當攻擊者開始用 AI 工業化擴張，防禦者如何用自動化、持續驗證與數位韌性重奪主動權。

**關鍵主題**

- AI 原生經濟與 82:1 人機混合勞動力
- Agentic AI 詐騙、深偽、提示詞注入與資料中毒
- 零信任 2.0、CTEM、Runtime 防護與 DevSecOps
- PQC、瀏覽器安全、SBOM、AI 治理與人才路徑

## 專案說明

本 Repository 為《2026 資安大轉折》的官方預覽網站。內容包含書籍介紹頁、全書總覽、13 章精選內容、出版提案包、作者介紹、試閱頁、購買預約與正式參考文獻，採用 GitHub Pages 進行發佈。

## 內容概覽

- 網站首頁：`docs/index.md`
- 全書總覽：`docs/book.md`
- 章節試閱：`docs/chapters/ch01.md` 到 `docs/chapters/ch13.md`
- 作者簡介：`docs/author.md`
- 試閱入口：`docs/preview.md`
- 購買資訊：`docs/buy.md`
- 參考文獻：`docs/references.md`
- 出版提案：`docs/proposal-package.md`
- 封面視覺：`docs/assets/images/cover-2026-cloud-security.svg`

## 章節導覽

- 第 1 章：2026，AI 經濟的新規則
- 第 2 章：防衛者之年：重奪主動權
- 第 3 章：自動化詐騙的崛起：從社交工程到 AI 代理
- 第 4 章：操控 AI 的攻擊：提示詞注入與資料中毒
- 第 5 章：地緣政治與新型網路犯罪
- 第 6 章：零信任 2.0：NSA 實作指引與持續驗證
- 第 7 章：雲端原生安全的成熟度缺口
- 第 8 章：持續威脅暴露管理與韌性指標
- 第 9 章：量子加密與加密敏捷性
- 第 10 章：瀏覽器：企業的新作業系統與前門
- 第 11 章：供應鏈安全與軟體物料清單
- 第 12 章：AI 治理與法律責任
- 第 13 章：未來人才：學習地圖與專業認證

## 線上閱讀結構

1. 從 `docs/index.md` 進入出版頁首頁。
2. 在 `docs/preview.md` 進入正式試閱入口。
3. 在 `docs/book.md` 查看整體定位與全書架構。
4. 進入各章獨立頁面閱讀試閱內容。
5. 在 `docs/references.md` 查看逐章正式參考文獻。
6. 在 `docs/proposal-package.md` 取得作者模板、封面文案與試閱 opening。

## 補充資源

- `docs/references.md`：逐章正式參考文獻頁。
- `docs/external-references-template.md`：逐章外部正式引用清單模板。
- `docs/assets/images/cover-2026-cloud-security.svg`：GitHub Pages 首頁使用的封面視覺檔。
- `docs/assets/main.scss`：首頁與整體網站的自訂樣式。

## 部署說明

1. 將此資料夾推送到 GitHub Repository。
2. 到 Repository 的 `Settings > Pages`。
3. 在 `Build and deployment` 選擇 `Deploy from a branch`。
4. Branch 選擇 `main`，Folder 選擇 `/docs`。
5. 儲存後，GitHub Pages 會以 `docs/index.md` 作為網站首頁。

### 本地預覽建議

- 若只需快速檢視 Markdown，可直接在 VS Code 預覽。
- 若要模擬 GitHub Pages，可使用 Jekyll 或任一靜態網站預覽工具讀取 `docs` 目錄。

## 網站結構

```text
.
├─ doc1
├─ README.md
└─ docs
	├─ _config.yml
	├─ author.md
	├─ preview.md
	├─ buy.md
	├─ external-references-template.md
	├─ index.md
	├─ book.md
	├─ references.md
	├─ proposal-package.md
	├─ assets
	│	├─ images
	│	│	└─ cover-2026-cloud-security.svg
	│	└─ main.scss
	└─ chapters
		├─ ch01.md
		├─ ch02.md
		├─ ch03.md
		├─ ch04.md
		├─ ch05.md
		├─ ch06.md
		├─ ch07.md
		├─ ch08.md
		├─ ch09.md
		├─ ch10.md
		├─ ch11.md
		├─ ch12.md
		└─ ch13.md
```

## 後續可擴充項目

1. 加入作者姓名、封面圖片與正式購買連結。
2. 補上案例研究、圖表與引用來源的頁碼格式。
3. 若要正式對外，可增加媒體引用、版本紀錄與英文摘要。