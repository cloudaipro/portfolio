### **深度學習、機器學習與數據挖掘**

- **股市分析：**
  - 建立 LSTM、TabNet及 LightGBM等模型，以美國股市10年資料進行訓練，預測未來股價
  - 使用近200 技術指標及複合式指標，建立可靠的操作策略
  ![image](https://github.com/user-attachments/assets/931e9268-00a6-408f-b818-981cd65557d8)

- **獲獎的數據挖掘產品：** 開發了一個數據挖掘產品，在首屆創新軟件系統比賽中獲得“優秀作品”獎。

---

### **MES (Manufacturing Execution Systems)系統設計**
- **MES Modeling**
  - Formulation management:建立生產配方，確保藥品生產的一致性和準確性。
![{C2D2D73B-D706-4C9E-801C-2A63DE1664AA}](https://github.com/user-attachments/assets/bdde880f-0502-4a96-9cd7-4adb6b8532cb)
  - Raw material specification management: 原物料產品規格定義
  - Lot management: Manage your products, formulation, raw/package materials, and recipes
  - Capsule In-Process Control： 即時監控生產流程，確保膠囊等產品的一致性與品質。
![{FF9B1962-464F-41C6-BC15-2D50C2A8F926}](https://github.com/user-attachments/assets/fe8a06d5-ea37-426a-a252-a191680be2fe)
  - Weighing and dispensing Control: 確保批次和整批的製造流程嚴格符合要求
  - 
  
- **Production Planning:** 依據銷售狀況，預估即將缺貨或已缺貨的產品，以及下一批次的生產量。生產批次依優先順序排列
- **Access Control:** 允許不同的使用者根據其工作職能擁有不同層級的存取權限。
  - Employee management: 基本員工資料管理，如帳號、密碼、職位、簽名檔等
  - Group management: 群組(角色)定義，設定人員與群組關係
  - Security control:設定群組、使用者相對應層級的存取權限
  ![{25B428E3-2ED1-4719-B876-071FDD5ACAC2}](https://github.com/user-attachments/assets/c872e467-c669-44c1-84b2-03c20faedf5e)

- **Raw Material Management**
  - 原物料庫存管理與使用紀錄追蹤
  - COA (Certificate of Analysis)/receiving report/retesting report 等文件管理
  - Confirmatory testing: 分析收集的樣本以更深入地了解供應商品質。

- **Product Management**
  - Finished Product Analysis: 根據藥典（例如 EP、USP、BP 和 JP）和規格執行全面的品質控制測試, 確保最終產品符合安全和有效性的標準
  ![{F3600417-47D8-4734-A9C9-D99C22997473}](https://github.com/user-attachments/assets/614f33e4-2a29-432d-84cc-433aea3539a1)
  - Stability Study: 執行穩定性研究，確認產品在一段時間內能夠保持其品質。
  - Test Definition: 定義產品每個成分, 所使用的測試方法與規格
  ![{09623CC9-8D92-4AE2-8D42-FD8524C1110A}](https://github.com/user-attachments/assets/b550bc69-462e-403e-ab74-a101fcbc90ae)
  - Recall Management: 針對有問題的產品批次，寄送recall 信件給客戶，追蹤recall 執行效率
  - Finihsed Product Cost Analysis: 依據原物料與包裝材購買成本，計算出每個生產批次的成本
---
### **採購系統**
  - Request Analysis(採購需求分析):即將缺貨或已缺貨的產品，根據預估量，計算出所需要的原物料，列出短缺的原物料與其相對應的規格，生產規劃人員可根據需求，將所需購買的原物料，送出採購需求單
  - Purchase Request Management: 依據需求單，系統會列出相對應的規格選項、符合廠商資料、採購紀錄與價錢，在完成詢價後，送出 purchase order(採購訂單)
  - Purchase Order Management: 訂單進度追蹤，如採購中、運送中、接收完成等。

---
### **實驗室系統 (Laboratory Management)**
  - Test Method Database:
  ![{5A057D5B-3A93-4979-B9CE-A540D65DDCEA}](https://github.com/user-attachments/assets/dc2226fa-e387-4dda-8422-8391424fe7e0)
    - 定義每個成分的測試方法與SOP
    - 版本控制:每次修正完成的版本，均賦予一個版本號碼
    - 審核機制管控:分成[review request]與[approved]兩個狀態，測試人員只能使用 [approved] 的 Test Method
  - Test Request: 依據需要，定義測試需求，如成分名稱、測試方法、測試規格等
  - Test Analysis:
    - 實驗室人員依據測試需求，進行實驗，紀錄實驗結果。
    - 審核機制: 測試完，進入[review request]，審核結果分為:[PASS],[Out of Spec.],[REDO]
    ![{9DBA523C-3BAA-43BB-A531-404B1862BEA6}](https://github.com/user-attachments/assets/6be9340e-d2ce-4f4f-a0e6-baf1d7860998)
  - Test Report: 依據測試結果，產生CoA(Certificate of Analysis)，寄送email給客戶

---
### **POS系統與電子商務網站**

- **POS系統：** 開發了功能強大的POS系統，包含以下特色：
  - **自動化發票生成：** 整合**EDI**及電子商務網站訂單，自動生成 pos 訂單，簡化外部訂單生成流程，減少手動工作量並降低錯誤風險。
  - **直觀UI設計：** 設計一個整合各項資訊與提醒功能，操作簡單直觀
  - **訂單管理:** 訂單流程管理，如理貨、出貨、寄發發票等
  - **客戶管理：** 客戶基本資料管理、折扣設定、發票歷史紀錄等。
  - **Back Order:** 針對缺貨產品，紀錄back order，代新產品補完貨，可email 通知客戶，詢問是否購買
  - **折扣方案管理:** 定義折扣方案內容，如適用產品、折扣期間、折扣額度與適用客戶等
  - **經銷商、業務人員績效管理:** 計算出每個業務人員每個月的業績、與獎金
  - **產品定價管理系統:** 定義每個產品的 MSR、經銷商價與員工價
- **庫存管理：**
  - 接收新產品
  - 隔離區產品管理:接手的新產品，需先進入隔離區，帶品管與測試人員，確保無誤，才可成正式產品發售
  - 產品庫存管理:庫存維護，如庫存調整、報廢、暫停銷售、調回隔離區等

- **電子商務網站開發：** 建立了一個以用戶為中心的電子商務平台，具備以下功能：
  - **購物車功能：**
  - **內容管理系統（CMS）：** 提供簡便的更新工具，方便更新產品列表、網站內容等，保持網站的活力與相關性。
    
---
### **工廠自動化與即時品質控制**
- **機台自動化:** 依據CIM SECS 或 inline 規格，設計機台自動化程式
- **專有即時品質控制系統(Real time quality control system)：** 開發了一個**即時品質控制系統**，設計“缺陷特徵”(defect feature)算法，進行海量數據的即時分析，有效提升了產品的良率。
  ![{53E8C8F6-C203-461A-BD27-66E720708D17}](https://github.com/user-attachments/assets/3e4ab463-3799-482c-99b6-a43b9ce89a37)
  - Defect Feature（DF）設計：將與品質監控有關之資訊抽離出來，只需小量記憶體，可常駐在記憶體，提升即時監控之效能
  - Defect Loader：負責接收機台檢測資料，並將其轉換成defect feature，寫入RTQCS DB中
  - Defect Feature 分析程式: 根據事先定義好的規則，即時監控廠內所有各種Defect狀況，若有異常則即時alarm
  - Judge Defect Tool: 提供對INLINE AOI Defect，作進一步的分析與重判
  - Central Quality Monitor(CQM): 即時監控廠內所有各種Defect狀況和特性值規格，以整合性方式顯示，若有異常則即時alarm

- **故障檢測與分類（Fault Detection and Classification）：**
  ![image](https://github.com/user-attachments/assets/ca72018c-be49-4e4a-a5f0-953bc220b26f)
  - FDCConsole主程式：負責接收Data Collection送來之資料，並根據user事先設定之FDCRule，check是否發生alarm，若發生alarm將該alarm寫入APC DB中
  -	APC DB：存放FDCRule、FDCRuleApply、Alarm及TraceData等等
  -	APC Website：為user之使用介面，含Trace Data查詢、Alarm Data查詢
  - APCDesigner：提供給user之rule建立的介面，可根據FDCFunction、DPMethod及歷史資料建立FDCRule model，再將該FDCRule Model依據機台與recipe建立FDCRuleApply
---
#### **手機 app 開發**
- Simply Scanner(https://apps.apple.com/us/app/simply-scanner-pdf-docs-scan/id1619943223)
![{758BB3BF-02FC-4B90-8573-692F8FA846B3}](https://github.com/user-attachments/assets/3e5b6805-f984-427d-a6be-d2ac163b6b74)
- Sudo Master(https://apps.apple.com/us/app/sudoku-master-puzzle-game/id6445899434)
![{04A0F296-5E2E-425D-888A-7CE39B690D8E}](https://github.com/user-attachments/assets/9a1cb47f-3fce-417f-9401-5cf1b7ae9b15)
- Tally Counter -digital counter(https://apps.apple.com/us/app/tally-counter-digital-counter/id1668011020)
![{14A6BDE8-F09E-4A67-BB2B-08984843541F}](https://github.com/user-attachments/assets/965f0e86-1364-4597-b75d-a4b325cb5a32)

---
