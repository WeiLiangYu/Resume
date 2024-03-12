# 論文名稱: 貝氏決策樹的效能與比較
此專案製作於中興大學統計研究所-碩士論文


指導教授：林長鋆<br>
研究生：魏良育<br>

文本內容：<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;透過SMOTE來生成少數類別的資料數。<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;評估在各種比例的不平衡資料下，各個貝氏模型的預測能力與效能。<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;套入實際資料進行模型效能比對。<br>
  
資料集：<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UCI machine learning repository - default of credit card clients <br>

不平衡資料處理方法：<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SMOTE

評估模型：<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Scikit Learn - DecisionTree<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Scikit Learn - RandomForest<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. G.Nuti(2021) - GMT Model (greedy-model tree)<br>

結論：<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;本篇論文當中，討論了三個不平衡資料經由SMOTE處理之後，GMT、決策樹與隨機森林模型的預測效果與性能。<br>
三個模型在經由SMOTE處理之後，預測能力都得到顯著的提升。GMT模型在資料不平衡比例未超過10000:100，即100:1時，雖然預測效果與決策樹的預測能力為差不多，但在少數類別的Precision分數上能比擬隨機森林。
即在判別為少數的資料中，實際上為少數的資料比率較高。而在不平衡的比率再進一步拉高時，GMT模型的預測能力比起其它兩個模型，預測能力稍顯較差。<br>
在模型模擬的速度方面，GMT比起單樹的決策樹來的慢一些，但遠快於集成學習的隨機森林，模擬速度差至近10倍。<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在第四章面對真實資料時，兩平衡資料的比率約為3:1，GMT預測資料的分數雖然不及其它兩個模型來的高。<br>
 但對於少數類別的預測，如同前節所模擬資料出來的結果一樣，Precision的分數可以達到與隨機森林相等的分數。
