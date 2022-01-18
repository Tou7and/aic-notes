# RASA Notes
整理一些 RASA 相關筆記


## Deployment
部署相關
- [Deploying Your Rasa Assistant](https://rasa.com/docs/rasa/how-to-deploy#using-your-custom-action-server-image)
- [Custom Rasa NLU Docker Containers](https://rasa.com/blog/custom-rasa-nlu-docker-container/)
- [Building a Rasa Assistant in Docker](https://rasa.com/docs/rasa/docker/building-in-docker/)
- [Deploying a Rasa Open Source Assistant in Docker Compose](https://rasa.com/docs/rasa/docker/deploying-in-docker-compose)


## RASA NLU
[List of components](https://rasa.com/docs/rasa/components/)


### 1 - Intent
- [rasa-intent-classification](https://rasa.com/blog/rasa-nlu-in-depth-part-1-intent-classification/)
- introduce how to choose proper intent classification pipelines


### 2 - Entity
[rasa-nlu-entity-recognition](https://rasa.com/blog/rasa-nlu-in-depth-part-2-entity-recognition/)
- introduce how to choose proper NER pipelines


### 3 - Hyper-parameters
[rasa-nlu-hyperparameter-optimization](https://rasa.com/blog/rasa-nlu-in-depth-part-3-hyperparameters/)
- 說明如何爆調一波參數
  - 設定參數範圍
  - 測試指標的定義與設定
- 透過 local 端 / k8s / docker-compose 執行 evaluation


### 4 - Error Handling
交談中的例外與錯誤處理 (deal with unhappy path)
- [Fallback: ensure your assistant fail gracefully](https://rasa.com/docs/rasa/fallback-handoff)


## RASA Actions
[RASA-Actions-SDK](https://rasa.com/docs/action-server/sdk-actions)


## Advanced Topics

[Contextual Conversations](https://rasa.com/docs/rasa/contextual-conversations)


## Examples

[RASA-medical-diagnosis-bot](https://paulminogue.com/index.php/2020/04/26/using-the-rasa-framework-to-implement-a-simple-medical-diagnosis-bot/)
> 用 rasa 實作初步醫療診斷聊天機器人
- 透過 NER 擷取症狀實體
- 症狀匹配
- 疾病分類: 用症狀序列作為特徵
  - 疾病分類 ML 模型 (decisiion tree) 可以參考 [itachi9604/healthcare-chatbot](https://github.com/itachi9604/healthcare-chatbot)


## Others
[Five Levels of AI Assistants in Enterprise](https://rasa.com/blog/conversational-ai-your-guide-to-five-levels-of-ai-assistants-in-enterprise/)
> 2018, RASA Blog
> 聊天機器人的發展階段(假說?)
- Level 1: Notification Assistants (Last 10 years)
- Level 2: FAQ Assistants (Now)
- Level 3: Contextual Assistants (Within 2 years)
- Level 4: Personalized Assistants (In 3-5 years)
- Level 5: Autonomous Organization of Assistants (In 10 years)



