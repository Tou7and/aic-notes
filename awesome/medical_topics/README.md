## Medical Speech Recognition

[speech recognition for medical conversation](https://arxiv.org/pdf/1711.07274.pdf)
ASR Systems for transcribing doctor-patient conversations, 2018, Google
- CTC: WER 20.1%
- LAS: WER 18.3%
- Trained on 14,000 hours of medical conversation
- Dataset split by speakers, no doctor overlap, male:female = 1:1

[Assessing the accuracy of automatic speech recognition for psychotherapy](https://www.nature.com/articles/s41746-020-0285-8#Sec7)
2020, Nature, Google ASR, Li Fei-Fei & Nigam H. Shah
- 針對輔助心理治療的語音技術進行評估(use Google ASR)
- For clinician-identified harm-related sentences, the word error rate was 34%
- Domain Agnostic Metric: WER
- Clinically-relevant Metric: [F1, Precision, Recall on PHQ9](https://www.nature.com/articles/s41746-020-0285-8/tables/3)
- Detail about corpus: [corpus creation process, annotation protocols](https://static-content.springer.com/esm/art%3A10.1038%2Fs41746-020-0285-8/MediaObjects/41746_2020_285_MOESM1_ESM.pdf)

[Design and Implementation of Cyrillic Mongolian Speech Input System for Thyroid Ultrasound Report](https://iopscience.iop.org/article/10.1088/1757-899X/768/7/072008/pdf)
- 語音超音波報告
- Speech input system: 自動載入病人資料及接收醫生語音輸入
- Cyrillic Mongolian Speech Recognition System: 蒙古 ASR
- Thyriod ultrasound reporting: 報告產生系統並含有載入相關病患資料以及歷史報告的功能
- CNN baseline / Dropout / Maxout

[Medical Speech Recognition:Reaching Parity with Humans](https://link.springer.com/chapter/10.1007/978-3-319-66429-3_51)
2017, SPECOM
- 270 小時的醫學語音數據+臨床事件文本
- WER ~ 16%

[A systematic comparison of contemporary automatic speech recognition engines for conversational clinical speech](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6371385/)
2018 AMIA Annu Symp Proc
- 臨床會話語音的系統 Benchmark
- 無腳本臨床場景錄製
- WER / Precision / Recall / F1

