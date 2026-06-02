# prompt1
Necesito que realices la siguiente actividad: "expandirnos a 20 fuentes bibliográficas, por lo que tenemos que buscar otras 15 aparte de las 5 que ya tenemos."

Las 5 fuentes que ya las tengo en formato bibtex:
```latex
@article{Kim2006,
   abstract = {While naive Bayes is quite effective in various data mining tasks, it shows a disappointing result in the automatic text classification problem. Based on the observation of naive Bayes for the natural language text, we found a serious problem in the parameter estimation process, which causes poor results in text classification domain. In this paper, we propose two empirical heuristics: per-document text normalization and feature weighting method. While these are somewhat ad hoc methods, our proposed naive Bayes text classifier performs very well in the standard benchmark collections, competing with state-of-the-art text classifiers based on a highly complex learning method such as SVM. © 2006, IEEE. All rights reserved.},
   author = {Sang Bum Kim and Kyoung Soo Han and Hae Chang Rim and Sung Hyon Myaeng},
   doi = {10.1109/TKDE.2006.180},
   issn = {10414347},
   issue = {11},
   journal = {IEEE Transactions on Knowledge and Data Engineering},
   keywords = {Poisson model,Text classification,feature weighting,naive Bayes classifier},
   month = {11},
   pages = {1457-1466},
   title = {Some effective techniques for naive bayes text classification},
   volume = {18},
   url = {https://ieeexplore.ieee.org/document/1704799},
   year = {2006}
}
@article{Sangounpao2019,
   abstract = {Content less than two hundred words like comments or review statements is known as a short text. Short text classification is useful for automatically categorizing sentence into predefined group. There are several traditional short text classification methods by using bag-of-words with k nearest neighbors (k-NN), Naïve Bayes, Maximum entropy, support vector machines (SVMs), and an algorithm based on statistics and rules. The deep learning method is outperformed other methods on classification of short text with normal size of dataset. Some researches classify requirements into functional and nonfunctional requirements. There is no research on multi-classification of functional requirements with a small dataset particularly for an accounting field. This paper presents an approach to classify short text for a small dataset into multiple categories of functional requirements on the accounting domain. The proposed approach uses an ontology to construct bag-of-words and uses Naive Bayes to classify for small dataset. The experiment is conducted using four hundred of datasets with 5folds and 10-folds cross-validation. The result shows that the method can correctly classify more than 80%. Additionally, comparisons between the ontology-based Naive Bayes method and other methods are investigated.},
   author = {Ketkaew Sangounpao and Pornsiri Muenchaisri},
   doi = {10.1109/SNPD.2019.8935711},
   isbn = {9781728116518},
   journal = {Proceedings - 20th IEEE/ACIS International Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing, SNPD 2019},
   keywords = {accounting domain knowledge,multi-classification,ontology,requirements engineering,short text classification,small dataset,traditional classification},
   month = {7},
   pages = {53-58},
   publisher = {Institute of Electrical and Electronics Engineers Inc.},
   title = {Ontology-Based Naive Bayes Short Text Classification Method for a Small Dataset},
   url = {https://ieeexplore.ieee.org/document/8935711},
   year = {2019}
}
@article{Frank2006,
   abstract = {Multinomial naive Bayes (MNB) is a popular method for document classification due to its computational efficiency and relatively good predictive performance. It has recently been established that predictive performance can be improved further by appropriate data...},
   author = {Eibe Frank and Remco R. Bouckaert},
   doi = {10.1007/11871637_49},
   isbn = {978-3-540-46048-0},
   issn = {1611-3349},
   journal = {Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)},
   pages = {503-510},
   publisher = {Springer, Berlin, Heidelberg},
   title = {Naive Bayes for Text Classification with Unbalanced Classes},
   volume = {4213 LNAI},
   url = {https://link.springer.com/chapter/10.1007/11871637_49},
   year = {2006}
}
@article{Zhang2016,
   abstract = {How can we know whether one classifier is really better than the other? In the area of text classification, since the publication of Yang and Liu's seminal SIGIR-1999 paper, it has become a standard practice for researchers to apply nullhypothesis significance testing (NHST) on their experimental results in order to establish the superiority of a classifier. However, such a frequentist approach has a number of inherent deficiencies and limitations, e.g., the inability to accept the null hypothesis (that the two classifiers perform equally well), the difficulty to compare commonly-used multivariate performance measures like F1 scores instead of accuracy, and so on. In this paper, we propose a novel Bayesian approach to the performance comparison of text classifiers, and argue its advantages over the traditional frequentist approach based on t-test etc. In contrast to the existing probabilistic model for F1 scores which is unpaired, our proposed model takes the correlation between classifiers into account and thus achieves greater statistical power. Using several typical text classification algorithms and a benchmark dataset, we demonstrate that the our approach provides rich information about the difference between two classifiers' performances.},
   author = {Dell Zhang and Jun Wang and Emine Yilmaz and Xiaoling Wang and Yuxin Zhou},
   doi = {10.1145/2911451.2911547;SUBPAGE:STRING:BASIC},
   isbn = {9781450342902},
   journal = {SIGIR 2016 - Proceedings of the 39th International ACM SIGIR Conference on Research and Development in Information Retrieval},
   keywords = {Bayesian inference,Hypothesis testing,Performance evaluation,Text classification},
   month = {7},
   pages = {15-24},
   publisher = {Association for Computing Machinery, Inc},
   title = {Bayesian performance comparison of text classifiers},
   url = {/doi/pdf/10.1145/2911451.2911547?download=true},
   year = {2016}
}
@article{Jiang2016,
   abstract = {Naive Bayes (NB) continues to be one of the top 10 data mining algorithms due to its simplicity, efficiency and efficacy. Of numerous proposals to improve the accuracy of naive Bayes by weakening its feature independence assumption, the feature weighting approach has received less attention from researchers. Moreover, to our knowledge, all of the existing feature weighting approaches only incorporate the learned feature weights into the classification of formula of naive Bayes and do not incorporate the learned feature weights into its conditional probability estimates at all. In this paper, we propose a simple, efficient, and effective feature weighting approach, called deep feature weighting (DFW), which estimates the conditional probabilities of naive Bayes by deeply computing feature weighted frequencies from training data. Empirical studies on a collection of 36 benchmark datasets from the UCI repository show that naive Bayes with deep feature weighting rarely degrades the quality of the model compared to standard naive Bayes and, in many cases, improves it dramatically. Besides, we apply the proposed deep feature weighting to some state-of-the-art naive Bayes text classifiers and have achieved remarkable improvements.},
   author = {Liangxiao Jiang and Chaoqun Li and Shasha Wang and Lungan Zhang},
   doi = {10.1016/J.ENGAPPAI.2016.02.002},
   issn = {0952-1976},
   journal = {Engineering Applications of Artificial Intelligence},
   keywords = {Correlation-based feature selection,Feature weighting,Naive Bayes,Text classification},
   month = {6},
   pages = {26-39},
   publisher = {Pergamon},
   title = {Deep feature weighting for naive Bayes and its application to text classification},
   volume = {52},
   url = {https://www.sciencedirect.com/science/article/abs/pii/S0952197616300112?via%3Dihub},
   year = {2016}
}
```

Las 5 fuentes que ya las tengo como referencia IEEE en markdown:
```markdown
\[1\] S. B. Kim, K. S. Han, and H. C. Rim, “Some effective techniques for naive bayes text classification,” IEEE Transactions on Knowledge and Data Engineering, vol. 18, no. 11, pp. 1457–1466, Nov. 2006, doi: 10.1109/TKDE.2006.180.

\[2\] K. Sangounpao and P. Muenchaisri, “Ontology-Based Naive Bayes Short Text Classification Method for a Small Dataset,” in Proc. 20th IEEE/ACIS Int. Conf. on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing (SNPD), Toyama, Japan, 2019, pp. 53–58, doi: 10.1109/SNPD.2019.8935711.

\[3\] E. Frank and R. R. Bouckaert, “Naïve Bayes for text classification with unbalanced classes,” in Proc. 10th Eur. Conf. on Principles and Practice of Knowledge Discovery in Databases (PKDD), Berlin, Germany, 2006, pp. 503–510, doi: 10.1007/11871637\_49. 

\[4\] D. Zhang, J. Wang, E. Yilmaz, X. Wang, and Y. Zhou, “Bayesian performance comparison of text classifiers,” in Proc. 39th Int. ACM SIGIR Conf. on Research and Development in Information Retrieval (SIGIR), Pisa, Italy, 2016, pp. 15–24, doi: 10.1145/2911451.2911547. 

\[5\] L. Jiang, C. Li, S. Wang, and L. Zhang, “Deep feature weighting for naive Bayes and its application to text classification,” Engineering Applications of Artificial Intelligence, vol. 52, pp. 26–39, Jun. 2016, doi: 10.1016/j.engappai.2016.02.002.
```


Necesito que encuentres 15 articulos que me sirvan para responder esta pregunta "¿Qué tan efectivo es Naive Bayes en clasificación de texto?". 

Sitios en donde debes buscar (limítate solo a estos 5): [IEEE, ACM, Scopus, Springer, Science Direct]

Por cada uno de los articulos necesito que les adjuntes:
1. De cual de esas bases indexadas sacaste el artículo (IEEE, ACM, Scopus, Springer o Science Direct).
2. El script de busqueda que utilizaste para encontrar ese artículo específico en su base científica indexada. Para que no te confundas: Es ese texto de busqueda que solo contiene palabras clave y operadores como el OR, el AND y todas esas cosas de las busquedas avanzadas.

Al final me presentas los 15 articulos con su URL DOI (para dirigirme rápidamente al artículo) junto con los 2 puntos que te acabé de mencionar (de donde lo sacaste y su respectivo script de busqueda) en un bloque de codigo markdown para poder copiar su contenido. Tomate tu tiempo.

# prompt2
Necesito que me hagas un script en python que me devuelva un solo .bib a partir de un arreglo con los dois de los articulos cientificos el bib incluye tambien el abstract.
```python
dois = [
    "10.1007/3-540-45683-x_45",
    "10.1007/978-3-540-30586-6_76",
    "10.1007/978-3-540-71496-5_73",
    "10.1007/11871637_49",
    "10.1007/11735106_17",
    "10.1016/j.eswa.2008.06.054",
    "10.1016/j.proeng.2011.08.404",
    "10.1016/j.patrec.2015.07.028",
    "10.1016/j.patrec.2008.11.013",
    "10.1016/j.knosys.2016.02.017",
    "10.1016/j.engappai.2016.02.002",
    "10.1016/j.asoc.2020.106652",
    "10.1016/j.knosys.2010.04.004",
    "10.1016/j.neucom.2018.07.002",
    "10.5555/1619645.1619732"
]
```

# prompt3
necesito que busques 1 solo arículo más ya que el siguiente artículo de los 15 que encontraste se repetía con uno que yo ya tenía en mis 5 artículos iniciales:
```bibtex
@InProceedings{10.1007/11871637_49,
author="Frank, Eibe
and Bouckaert, Remco R.",
editor="F{\"u}rnkranz, Johannes
and Scheffer, Tobias
and Spiliopoulou, Myra",
title="Naive Bayes for Text Classification with Unbalanced Classes",
booktitle="Knowledge Discovery in Databases: PKDD 2006",
year="2006",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="503--510",
abstract="Multinomial naive Bayes (MNB) is a popular method for document classification due to its computational efficiency and relatively good predictive performance. It has recently been established that predictive performance can be improved further by appropriate data transformations [1,2]. In this paper we present another transformation that is designed to combat a potential problem with the application of MNB to unbalanced datasets. We propose an appropriate correction by adjusting attribute priors. This correction can be implemented as another data normalization step, and we show that it can significantly improve the area under the ROC curve. We also show that the modified version of MNB is very closely related to the simple centroid-based classifier and compare the two methods empirically.",
isbn="978-3-540-46048-0",
doi = {https://doi.org/10.1007/11871637_49}
}
```

# prompt4
Mira si no tengo ningun duplicado:
```bibtex
@article{Kim2006,
   abstract = {While naive Bayes is quite effective in various data mining tasks, it shows a disappointing result in the automatic text classification problem. Based on the observation of naive Bayes for the natural language text, we found a serious problem in the parameter estimation process, which causes poor results in text classification domain. In this paper, we propose two empirical heuristics: per-document text normalization and feature weighting method. While these are somewhat ad hoc methods, our proposed naive Bayes text classifier performs very well in the standard benchmark collections, competing with state-of-the-art text classifiers based on a highly complex learning method such as SVM. © 2006, IEEE. All rights reserved.},
   author = {Sang Bum Kim and Kyoung Soo Han and Hae Chang Rim and Sung Hyon Myaeng},
   doi = {10.1109/TKDE.2006.180},
   issn = {10414347},
   issue = {11},
   journal = {IEEE Transactions on Knowledge and Data Engineering},
   keywords = {Poisson model,Text classification,feature weighting,naive Bayes classifier},
   month = {11},
   pages = {1457-1466},
   title = {Some effective techniques for naive bayes text classification},
   volume = {18},
   url = {https://ieeexplore.ieee.org/document/1704799},
   year = {2006}
}
@article{Sangounpao2019,
   abstract = {Content less than two hundred words like comments or review statements is known as a short text. Short text classification is useful for automatically categorizing sentence into predefined group. There are several traditional short text classification methods by using bag-of-words with k nearest neighbors (k-NN), Naïve Bayes, Maximum entropy, support vector machines (SVMs), and an algorithm based on statistics and rules. The deep learning method is outperformed other methods on classification of short text with normal size of dataset. Some researches classify requirements into functional and nonfunctional requirements. There is no research on multi-classification of functional requirements with a small dataset particularly for an accounting field. This paper presents an approach to classify short text for a small dataset into multiple categories of functional requirements on the accounting domain. The proposed approach uses an ontology to construct bag-of-words and uses Naive Bayes to classify for small dataset. The experiment is conducted using four hundred of datasets with 5folds and 10-folds cross-validation. The result shows that the method can correctly classify more than 80%. Additionally, comparisons between the ontology-based Naive Bayes method and other methods are investigated.},
   author = {Ketkaew Sangounpao and Pornsiri Muenchaisri},
   doi = {10.1109/SNPD.2019.8935711},
   isbn = {9781728116518},
   journal = {Proceedings - 20th IEEE/ACIS International Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing, SNPD 2019},
   keywords = {accounting domain knowledge,multi-classification,ontology,requirements engineering,short text classification,small dataset,traditional classification},
   month = {7},
   pages = {53-58},
   publisher = {Institute of Electrical and Electronics Engineers Inc.},
   title = {Ontology-Based Naive Bayes Short Text Classification Method for a Small Dataset},
   url = {https://ieeexplore.ieee.org/document/8935711},
   year = {2019}
}
@article{Frank2006,
   abstract = {Multinomial naive Bayes (MNB) is a popular method for document classification due to its computational efficiency and relatively good predictive performance. It has recently been established that predictive performance can be improved further by appropriate data...},
   author = {Eibe Frank and Remco R. Bouckaert},
   doi = {10.1007/11871637_49},
   isbn = {978-3-540-46048-0},
   issn = {1611-3349},
   journal = {Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)},
   pages = {503-510},
   publisher = {Springer, Berlin, Heidelberg},
   title = {Naive Bayes for Text Classification with Unbalanced Classes},
   volume = {4213 LNAI},
   url = {https://link.springer.com/chapter/10.1007/11871637_49},
   year = {2006}
}
@inproceedings{10.1145/2911451.2911547,
author = {Zhang, Dell and Wang, Jun and Yilmaz, Emine and Wang, Xiaoling and Zhou, Yuxin},
title = {Bayesian Performance Comparison of Text Classifiers},
year = {2016},
isbn = {9781450340694},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/2911451.2911547},
doi = {10.1145/2911451.2911547},
abstract = {How can we know whether one classifier is really better than the other? In the area of text classification, since the publication of Yang and Liu's seminal SIGIR-1999 paper, it has become a standard practice for researchers to apply null-hypothesis significance testing (NHST) on their experimental results in order to establish the superiority of a classifier. However, such a frequentist approach has a number of inherent deficiencies and limitations, e.g., the inability to accept the null hypothesis (that the two classifiers perform equally well), the difficulty to compare commonly-used multivariate performance measures like F1 scores instead of accuracy, and so on. In this paper, we propose a novel Bayesian approach to the performance comparison of text classifiers, and argue its advantages over the traditional frequentist approach based on t-test etc. In contrast to the existing probabilistic model for F1 scores which is unpaired, our proposed model takes the correlation between classifiers into account and thus achieves greater statistical power. Using several typical text classification algorithms and a benchmark dataset, we demonstrate that the our approach provides rich information about the difference between two classifiers' performances.},
booktitle = {Proceedings of the 39th International ACM SIGIR Conference on Research and Development in Information Retrieval},
pages = {15–24},
numpages = {10},
keywords = {bayesian inference, hypothesis testing, performance evaluation, text classification},
location = {Pisa, Italy},
series = {SIGIR '16}
}
@article{Jiang2016,
   abstract = {Naive Bayes (NB) continues to be one of the top 10 data mining algorithms due to its simplicity, efficiency and efficacy. Of numerous proposals to improve the accuracy of naive Bayes by weakening its feature independence assumption, the feature weighting approach has received less attention from researchers. Moreover, to our knowledge, all of the existing feature weighting approaches only incorporate the learned feature weights into the classification of formula of naive Bayes and do not incorporate the learned feature weights into its conditional probability estimates at all. In this paper, we propose a simple, efficient, and effective feature weighting approach, called deep feature weighting (DFW), which estimates the conditional probabilities of naive Bayes by deeply computing feature weighted frequencies from training data. Empirical studies on a collection of 36 benchmark datasets from the UCI repository show that naive Bayes with deep feature weighting rarely degrades the quality of the model compared to standard naive Bayes and, in many cases, improves it dramatically. Besides, we apply the proposed deep feature weighting to some state-of-the-art naive Bayes text classifiers and have achieved remarkable improvements.},
   author = {Liangxiao Jiang and Chaoqun Li and Shasha Wang and Lungan Zhang},
   doi = {10.1016/J.ENGAPPAI.2016.02.002},
   issn = {0952-1976},
   journal = {Engineering Applications of Artificial Intelligence},
   keywords = {Correlation-based feature selection,Feature weighting,Naive Bayes,Text classification},
   month = {6},
   pages = {26-39},
   publisher = {Pergamon},
   title = {Deep feature weighting for naive Bayes and its application to text classification},
   volume = {52},
   url = {https://www.sciencedirect.com/science/article/abs/pii/S0952197616300112?via%3Dihub},
   year = {2016}
}

@InProceedings{10.1007/3-540-45683-X_45,
author="Kim, Sang-Bum
and Rim, Hae-Chang
and Yook, DongSuk
and Lim, Heui-Seok",
editor="Ishizuka, Mitsuru
and Sattar, Abdul",
title="Effective Methods for Improving Naive Bayes Text Classifiers",
booktitle="PRICAI 2002: Trends in Artificial Intelligence",
year="2002",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="414--423",
abstract="Though naive Bayes text classifiers are widely used because of its simplicity, the techniques for improving performances of these classifiers have been rarely studied. In this paper, we propose and evaluate some general and effective techniques for improving performance of the naive Bayes text classifier. We suggest document model based parameter estimation and document length normalization to alleviate the problems in the traditional multinomial approach for text classification. In addition, Mutual-Information-weighted naive Bayes text classifier is proposed to increase the effect of highly informative words. Our techniques are evaluated on the Reuters21578 and 20 Newsgroups collections, and significant improvements are obtained over the existing multinomial naive Bayes approach.",
isbn="978-3-540-45683-4",
doi = {https://doi.org/10.1007/3-540-45683-X_45}
}

@InProceedings{10.1007/978-3-540-30586-6_76,
author="Schneider, Karl-Michael",
editor="Gelbukh, Alexander",
title="Techniques for Improving the Performance of Naive Bayes for Text Classification",
booktitle="Computational Linguistics and Intelligent Text Processing",
year="2005",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="682--693",
abstract="Naive Bayes is often used in text classification applications and experiments because of its simplicity and effectiveness. However, its performance is often degraded because it does not model text well, and by inappropriate feature selection and the lack of reliable confidence scores. We address these problems and show that they can be solved by some simple corrections. We demonstrate that our simple modifications are able to improve the performance of Naive Bayes for text classification significantly.",
isbn="978-3-540-30586-6",
doi = {https://doi.org/10.1007/978-3-540-30586-6_76}
}

@InProceedings{10.1007/978-3-540-71496-5_73,
author="He, Feng
and Ding, Xiaoqing",
editor="Amati, Giambattista
and Carpineto, Claudio
and Romano, Giovanni",
title="Improving Naive Bayes Text Classifier Using Smoothing Methods",
booktitle="Advances in Information Retrieval",
year="2007",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="703--707",
abstract="The performance of naive Bayes text classifier is greatly influenced by parameter estimation, while the large vocabulary and scarce labeled training set bring difficulty in parameter estimation. In this paper, several smoothing methods are introduced to estimate parameters in naive Bayes text classifier. The proposed approaches can achieve better and more stable performance than Laplace smoothing.",
isbn="978-3-540-71496-5",
doi = {https://doi.org/10.1007/978-3-540-71496-5_73}
}

@article{FENG2015109,
title = {Feature subset selection using naive Bayes for text classification},
journal = {Pattern Recognition Letters},
volume = {65},
pages = {109-115},
year = {2015},
issn = {0167-8655},
doi = {https://doi.org/10.1016/j.patrec.2015.07.028},
url = {https://www.sciencedirect.com/science/article/pii/S0167865515002378},
author = {Guozhong Feng and Jianhua Guo and Bing-Yi Jing and Tieli Sun},
keywords = {Bayesian model averaging, Global selection index, Latent selection augmented naive Bayes, Local selection index, Text classification},
abstract = {Feature subset selection is known to improve text classification performance of various classifiers. The model using the selected features is often regarded as if it had generated the data. By taking its uncertainty into account, the discrimination capabilities can be measured by a global selection index (GSI), which can be used in the prediction function. In this paper, we propose a latent selection augmented naive (LSAN) Bayes classifier. By introducing a latent feature selection indicator, the GSI can be factorized into each local selection index (LSI). Using conjugate priors, the LSI for feature evaluation can be explicitly calculated. Then the feature subset selection models can be pruned by thresholding the LSIs, and the LSAN classifier can be achieved by the product of a small percentage of single feature model averages. The numerical results on some real datasets show that the proposed method outperforms the contrast feature weighting methods, and is very competitive if compared with some other commonly used classifiers such as SVM.}
}

@InProceedings{10.1007/11735106_17,
author="Yin, Ling
and Power, Richard",
editor="Lalmas, Mounia
and MacFarlane, Andy
and R{\"u}ger, Stefan
and Tombros, Anastasios
and Tsikrika, Theodora
and Yavlinsky, Alexei",
title="Adapting the Naive Bayes Classifier to Rank Procedural Texts",
booktitle="Advances in Information Retrieval",
year="2006",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="179--190",
abstract="This paper presents a machine-learning approach for ranking web documents according to the proportion of procedural text they contain. By `procedural text' we refer to ordered lists of steps, which are very common in some instructional genres such as online manuals. Our initial training corpus is built up by applying some simple heuristics to select documents from a large collection and contains only a few documents with a large proportion of procedural texts. We adapt the Naive Bayes classifier to better fit this less than ideal training corpus. This adapted model is compared with several other classifiers in ranking procedural texts using different sets of features and is shown to perform well when only highly distinctive features are used.",
isbn="978-3-540-33348-7",
doi = {https://doi.org/10.1007/11735106_17}
}

@article{CHEN20095432,
title = {Feature selection for text classification with Naïve Bayes},
journal = {Expert Systems with Applications},
volume = {36},
number = {3, Part 1},
pages = {5432-5435},
year = {2009},
issn = {0957-4174},
doi = {https://doi.org/10.1016/j.eswa.2008.06.054},
url = {https://www.sciencedirect.com/science/article/pii/S0957417408003564},
author = {Jingnian Chen and Houkuan Huang and Shengfeng Tian and Youli Qu},
keywords = {Text classification, Feature selection, Text preprocessing, Naïve Bayes},
abstract = {As an important preprocessing technology in text classification, feature selection can improve the scalability, efficiency and accuracy of a text classifier. In general, a good feature selection method should consider domain and algorithm characteristics. As the Naïve Bayesian classifier is very simple and efficient and highly sensitive to feature selection, so the research of feature selection specially for it is significant. This paper presents two feature evaluation metrics for the Naïve Bayesian classifier applied on multi-class text datasets: Multi-class Odds Ratio (MOR), and Class Discriminating Measure (CDM). Experiments of text classification with Naïve Bayesian classifiers were carried out on two multi-class texts collections. As the results indicate, CDM and MOR gain obviously better selecting effect than other feature selection approaches.}
}

@article{ZHANG20112160,
title = {An Improvement to Naive Bayes for Text Classification},
journal = {Procedia Engineering},
volume = {15},
pages = {2160-2164},
year = {2011},
note = {CEIS 2011},
issn = {1877-7058},
doi = {https://doi.org/10.1016/j.proeng.2011.08.404},
url = {https://www.sciencedirect.com/science/article/pii/S1877705811019059},
author = {Wei Zhang and Feng Gao},
keywords = {Text classification, Feature selection, Machine learning, Naïve Bayes},
abstract = {Naïve Bayes classifiers which are widely used for text classification in machine learning are based on the conditional probability of features belonging to a class, which the features are selected by feature selection methods. In this paper, an auxiliary feature method is proposed. It determines features by an existing feature selection method, and selects an auxiliary feature which can reclassify the text space aimed at the chosen features. Then the corresponding conditional probability is adjusted in order to improve classification accuracy. Illustrative examples show that the proposed meth-od indeed improves the performance of naïve Bayes classifier.}
}

@article{FENG2015109,
title = {Feature subset selection using naive Bayes for text classification},
journal = {Pattern Recognition Letters},
volume = {65},
pages = {109-115},
year = {2015},
issn = {0167-8655},
doi = {https://doi.org/10.1016/j.patrec.2015.07.028},
url = {https://www.sciencedirect.com/science/article/pii/S0167865515002378},
author = {Guozhong Feng and Jianhua Guo and Bing-Yi Jing and Tieli Sun},
keywords = {Bayesian model averaging, Global selection index, Latent selection augmented naive Bayes, Local selection index, Text classification},
abstract = {Feature subset selection is known to improve text classification performance of various classifiers. The model using the selected features is often regarded as if it had generated the data. By taking its uncertainty into account, the discrimination capabilities can be measured by a global selection index (GSI), which can be used in the prediction function. In this paper, we propose a latent selection augmented naive (LSAN) Bayes classifier. By introducing a latent feature selection indicator, the GSI can be factorized into each local selection index (LSI). Using conjugate priors, the LSI for feature evaluation can be explicitly calculated. Then the feature subset selection models can be pruned by thresholding the LSIs, and the LSAN classifier can be achieved by the product of a small percentage of single feature model averages. The numerical results on some real datasets show that the proposed method outperforms the contrast feature weighting methods, and is very competitive if compared with some other commonly used classifiers such as SVM.}
}

@article{YOUN2009477,
title = {Class dependent feature scaling method using naive Bayes classifier for text datamining},
journal = {Pattern Recognition Letters},
volume = {30},
number = {5},
pages = {477-485},
year = {2009},
issn = {0167-8655},
doi = {https://doi.org/10.1016/j.patrec.2008.11.013},
url = {https://www.sciencedirect.com/science/article/pii/S0167865508003553},
author = {Eunseog Youn and Myong K. Jeong},
keywords = {Classification, Feature selection, Naive Bayes classifier, Recursive feature elimination},
abstract = {The problem of feature selection is to find a subset of features for optimal classification. A critical part of feature selection is to rank features according to their importance for classification. The naive Bayes classifier has been extensively used in text categorization. We have developed a new feature scaling method, called class–dependent–feature–weighting (CDFW) using naive Bayes (NB) classifier. A new feature scaling method, CDFW–NB–RFE, combines CDFW and recursive feature elimination (RFE). Our experimental results showed that CDFW–NB–RFE outperformed other popular feature ranking schemes used on text datasets.}
}

@article{ZHANG2016137,
title = {Two feature weighting approaches for naive Bayes text classifiers},
journal = {Knowledge-Based Systems},
volume = {100},
pages = {137-144},
year = {2016},
issn = {0950-7051},
doi = {https://doi.org/10.1016/j.knosys.2016.02.017},
url = {https://www.sciencedirect.com/science/article/pii/S0950705116001039},
author = {Lungan Zhang and Liangxiao Jiang and Chaoqun Li and Ganggang Kong},
keywords = {Naive Bayes text classifiers, Feature weighting, Gain ratio, Decision tree},
abstract = {This paper works on feature weighting approaches for naive Bayes text classifiers. Almost all existing feature weighting approaches for naive Bayes text classifiers have some defects: limited improvement to classification performance of naive Bayes text classifiers or sacrificing the simplicity and execution time of the final models. In fact, feature weighting is not new for machine learning community, and many researchers have made fruitful efforts in the field of feature weighting. This paper reviews some simple and efficient feature weighting approaches designed for standard naive Bayes classifiers, and adapts them for naive Bayes text classifiers. As a result, this paper proposes two adaptive feature weighting approaches for naive Bayes text classifiers. Experimental results based on benchmark and real-world data show that, compared to their competitors, our feature weighting approaches show higher classification accuracy, yet at the same time maintain the simplicity and lower execution time of the final models.}
}

@article{JIANG201626,
title = {Deep feature weighting for naive Bayes and its application to text classification},
journal = {Engineering Applications of Artificial Intelligence},
volume = {52},
pages = {26-39},
year = {2016},
issn = {0952-1976},
doi = {https://doi.org/10.1016/j.engappai.2016.02.002},
url = {https://www.sciencedirect.com/science/article/pii/S0952197616300112},
author = {Liangxiao Jiang and Chaoqun Li and Shasha Wang and Lungan Zhang},
keywords = {Naive Bayes, Feature weighting, Correlation-based feature selection, Text classification},
abstract = {Naive Bayes (NB) continues to be one of the top 10 data mining algorithms due to its simplicity, efficiency and efficacy. Of numerous proposals to improve the accuracy of naive Bayes by weakening its feature independence assumption, the feature weighting approach has received less attention from researchers. Moreover, to our knowledge, all of the existing feature weighting approaches only incorporate the learned feature weights into the classification of formula of naive Bayes and do not incorporate the learned feature weights into its conditional probability estimates at all. In this paper, we propose a simple, efficient, and effective feature weighting approach, called deep feature weighting (DFW), which estimates the conditional probabilities of naive Bayes by deeply computing feature weighted frequencies from training data. Empirical studies on a collection of 36 benchmark datasets from the UCI repository show that naive Bayes with deep feature weighting rarely degrades the quality of the model compared to standard naive Bayes and, in many cases, improves it dramatically. Besides, we apply the proposed deep feature weighting to some state-of-the-art naive Bayes text classifiers and have achieved remarkable improvements.}
}

@article{ELHINDI2020106652,
title = {Lazy fine-tuning algorithms for naïve Bayesian text classification},
journal = {Applied Soft Computing},
volume = {96},
pages = {106652},
year = {2020},
issn = {1568-4946},
doi = {https://doi.org/10.1016/j.asoc.2020.106652},
url = {https://www.sciencedirect.com/science/article/pii/S1568494620305901},
author = {Khalil M. {El Hindi} and Reem R. Aljulaidan and Hussien AlSalman},
keywords = {Fine-tuning Naïve Bayes, Document categorization, Local learning, Multinomial text classification, Complement NB, One-versus-all NB},
abstract = {The naïve Bayes (NB) learning algorithm is widely applied in many fields, particularly in text classification. However, its performance decreases when it is used in domains where its naïve assumption is violated or when the training set is too small to find accurate estimations of the probabilities. In this study, we propose a lazy fine-tuning naïve Bayes (LFTNB) method to address both problems. We propose a local fine-tuning algorithm that uses the nearest neighbors of a query instance to fine-tune the probability terms used by NB. Applying the nearest neighbors only makes the independence assumption more likely to be valid, whereas the fine-tuning algorithm is used to find more accurate estimations of the probability terms. The performance of the LFTNB approach was evaluated using 47 UCI datasets. The results show that the LFTNB method achieves superior performance than classical NB, eager FTNB, and k-nearest neighbor algorithms. We also propose eager and lazy fine-tuning versions of powerful NB-based text classification algorithms, namely, multinomial NB, complement NB, and one-versus-all NB. The empirical results using 18 UCI text classification datasets show that the proposed methods outperform untuned versions of these algorithms.}
}

@article{LU2010598,
title = {Chinese text classification by the Naïve Bayes Classifier and the associative classifier with multiple confidence threshold values},
journal = {Knowledge-Based Systems},
volume = {23},
number = {6},
pages = {598-604},
year = {2010},
issn = {0950-7051},
doi = {https://doi.org/10.1016/j.knosys.2010.04.004},
url = {https://www.sciencedirect.com/science/article/pii/S0950705110000638},
author = {Shing-Hwa Lu and Ding-An Chiang and Huan-Chao Keh and Hui-Hua Huang},
keywords = {Association classification, Text classification, Text mining, Text categorization},
abstract = {Each type of classifier has its own advantages as well as certain shortcomings. In this paper, we take the advantages of the associative classifier and the Naïve Bayes Classifier to make up the shortcomings of each other, thus improving the accuracy of text classification. We will classify the training cases with the Naïve Bayes Classifier and set different confidence threshold values for different class association rules (CARs) to different classes by the obtained classification accuracy rate of the Naïve Bayes Classifier to the classes. Since the accuracy rates of all selected CARs of the class are higher than that obtained by the Naïve Bayes Classifier, we could further optimize the classification result through these selected CARs. Moreover, for those unclassified cases, we will classify them with the Naïve Bayes Classifier. The experimental results show that combining the advantages of these two different classifiers better classification result can be obtained than with a single classifier.}
}

@article{KIM2018128,
title = {Towards perfect text classification with Wikipedia-based semantic Naïve Bayes learning},
journal = {Neurocomputing},
volume = {315},
pages = {128-134},
year = {2018},
issn = {0925-2312},
doi = {https://doi.org/10.1016/j.neucom.2018.07.002},
url = {https://www.sciencedirect.com/science/article/pii/S0925231218308282},
author = {Han-joon Kim and Jiyun Kim and Jinseog Kim and Pureum Lim},
keywords = {Text classification, Naïve Bayes learning, Tensor space, Wikipedia, Semantic features},
abstract = {This paper suggests a novel way of dramatically improving the Naïve Bayes text classifier with our semantic tensor space model for document representation. In our work, we intend to achieve a perfect text classification with the semantic Naïve Bayes learning that incorporates the semantic concept features into term feature statistics; for this, the Naïve Bayes learning is semantically augmented under the tensor space model where the ‘concept’ space is regarded as an independent space equated with the ‘term’ and ‘document’ spaces, and it is produced with concept-level informative Wikipedia pages associated with a given document corpus. Through extensive experiments using three popular document corpora including Reuters-21578, 20Newsgroups, and OHSUMED corpora, we prove that the proposed method not only has superiority over the recent deep learning-based classification methods but also shows nearly perfect classification performance.}
}

@inproceedings{10.5555/1619645.1619732,
author = {Dai, Wenyuan and Xue, Gui-Rong and Yang, Qiang and Yu, Yong},
title = {Transferring naive bayes classifiers for text classification},
year = {2007},
isbn = {9781577353232},
publisher = {AAAI Press},
abstract = {A basic assumption in traditional machine learning is that the training and test data distributions should be identical. This assumption may not hold in many situations in practice, but we may be forced to rely on a different-distribution data to learn a prediction model. For example, this may be the case when it is expensive to label the data in a domain of interest, although in a related but different domain there may be plenty of labeled data available. In this paper, we propose a novel transfer-learning algorithm for text classification based on an EM-based Naive Bayes classifiers. Our solution is to first estimate the initial probabilities under a distribution Dl of one labeled data set, and then use an EM algorithm to revise the model for a different distribution Du of the test data which are unlabeled. We show that our algorithm is very effective in several different pairs of domains, where the distances between the different distributions are measured using the Kullback-Leibler (KL) divergence. Moreover, KL-divergence is used to decide the trade-off parameters in our algorithm. In the experiment, our algorithm outperforms the traditional supervised and semi-supervised learning algorithms when the distributions of the training and test sets are increasingly different.},
booktitle = {Proceedings of the 22nd National Conference on Artificial Intelligence - Volume 1},
pages = {540–545},
numpages = {6},
location = {Vancouver, British Columbia, Canada},
series = {AAAI'07},
url = {https://dl.acm.org/doi/10.5555/1619645.1619732}
}
```

# prompt5
Ayudame a buscar otros 2 articulos por que como podrás ver en mis siguientes referencias hay 2 articulos duplicados. Te paso todos mis artículos para que no vuelvas a duplicar nada.
```bibtex
@article{Kim2006,
   abstract = {While naive Bayes is quite effective in various data mining tasks, it shows a disappointing result in the automatic text classification problem. Based on the observation of naive Bayes for the natural language text, we found a serious problem in the parameter estimation process, which causes poor results in text classification domain. In this paper, we propose two empirical heuristics: per-document text normalization and feature weighting method. While these are somewhat ad hoc methods, our proposed naive Bayes text classifier performs very well in the standard benchmark collections, competing with state-of-the-art text classifiers based on a highly complex learning method such as SVM. © 2006, IEEE. All rights reserved.},
   author = {Sang Bum Kim and Kyoung Soo Han and Hae Chang Rim and Sung Hyon Myaeng},
   doi = {10.1109/TKDE.2006.180},
   issn = {10414347},
   issue = {11},
   journal = {IEEE Transactions on Knowledge and Data Engineering},
   keywords = {Poisson model,Text classification,feature weighting,naive Bayes classifier},
   month = {11},
   pages = {1457-1466},
   title = {Some effective techniques for naive bayes text classification},
   volume = {18},
   url = {https://ieeexplore.ieee.org/document/1704799},
   year = {2006}
}
@article{Sangounpao2019,
   abstract = {Content less than two hundred words like comments or review statements is known as a short text. Short text classification is useful for automatically categorizing sentence into predefined group. There are several traditional short text classification methods by using bag-of-words with k nearest neighbors (k-NN), Naïve Bayes, Maximum entropy, support vector machines (SVMs), and an algorithm based on statistics and rules. The deep learning method is outperformed other methods on classification of short text with normal size of dataset. Some researches classify requirements into functional and nonfunctional requirements. There is no research on multi-classification of functional requirements with a small dataset particularly for an accounting field. This paper presents an approach to classify short text for a small dataset into multiple categories of functional requirements on the accounting domain. The proposed approach uses an ontology to construct bag-of-words and uses Naive Bayes to classify for small dataset. The experiment is conducted using four hundred of datasets with 5folds and 10-folds cross-validation. The result shows that the method can correctly classify more than 80%. Additionally, comparisons between the ontology-based Naive Bayes method and other methods are investigated.},
   author = {Ketkaew Sangounpao and Pornsiri Muenchaisri},
   doi = {10.1109/SNPD.2019.8935711},
   isbn = {9781728116518},
   journal = {Proceedings - 20th IEEE/ACIS International Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing, SNPD 2019},
   keywords = {accounting domain knowledge,multi-classification,ontology,requirements engineering,short text classification,small dataset,traditional classification},
   month = {7},
   pages = {53-58},
   publisher = {Institute of Electrical and Electronics Engineers Inc.},
   title = {Ontology-Based Naive Bayes Short Text Classification Method for a Small Dataset},
   url = {https://ieeexplore.ieee.org/document/8935711},
   year = {2019}
}
@article{Frank2006,
   abstract = {Multinomial naive Bayes (MNB) is a popular method for document classification due to its computational efficiency and relatively good predictive performance. It has recently been established that predictive performance can be improved further by appropriate data...},
   author = {Eibe Frank and Remco R. Bouckaert},
   doi = {10.1007/11871637_49},
   isbn = {978-3-540-46048-0},
   issn = {1611-3349},
   journal = {Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)},
   pages = {503-510},
   publisher = {Springer, Berlin, Heidelberg},
   title = {Naive Bayes for Text Classification with Unbalanced Classes},
   volume = {4213 LNAI},
   url = {https://link.springer.com/chapter/10.1007/11871637_49},
   year = {2006}
}
@inproceedings{10.1145/2911451.2911547,
author = {Zhang, Dell and Wang, Jun and Yilmaz, Emine and Wang, Xiaoling and Zhou, Yuxin},
title = {Bayesian Performance Comparison of Text Classifiers},
year = {2016},
isbn = {9781450340694},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/2911451.2911547},
doi = {10.1145/2911451.2911547},
abstract = {How can we know whether one classifier is really better than the other? In the area of text classification, since the publication of Yang and Liu's seminal SIGIR-1999 paper, it has become a standard practice for researchers to apply null-hypothesis significance testing (NHST) on their experimental results in order to establish the superiority of a classifier. However, such a frequentist approach has a number of inherent deficiencies and limitations, e.g., the inability to accept the null hypothesis (that the two classifiers perform equally well), the difficulty to compare commonly-used multivariate performance measures like F1 scores instead of accuracy, and so on. In this paper, we propose a novel Bayesian approach to the performance comparison of text classifiers, and argue its advantages over the traditional frequentist approach based on t-test etc. In contrast to the existing probabilistic model for F1 scores which is unpaired, our proposed model takes the correlation between classifiers into account and thus achieves greater statistical power. Using several typical text classification algorithms and a benchmark dataset, we demonstrate that the our approach provides rich information about the difference between two classifiers' performances.},
booktitle = {Proceedings of the 39th International ACM SIGIR Conference on Research and Development in Information Retrieval},
pages = {15–24},
numpages = {10},
keywords = {bayesian inference, hypothesis testing, performance evaluation, text classification},
location = {Pisa, Italy},
series = {SIGIR '16}
}
@article{Jiang2016,
   abstract = {Naive Bayes (NB) continues to be one of the top 10 data mining algorithms due to its simplicity, efficiency and efficacy. Of numerous proposals to improve the accuracy of naive Bayes by weakening its feature independence assumption, the feature weighting approach has received less attention from researchers. Moreover, to our knowledge, all of the existing feature weighting approaches only incorporate the learned feature weights into the classification of formula of naive Bayes and do not incorporate the learned feature weights into its conditional probability estimates at all. In this paper, we propose a simple, efficient, and effective feature weighting approach, called deep feature weighting (DFW), which estimates the conditional probabilities of naive Bayes by deeply computing feature weighted frequencies from training data. Empirical studies on a collection of 36 benchmark datasets from the UCI repository show that naive Bayes with deep feature weighting rarely degrades the quality of the model compared to standard naive Bayes and, in many cases, improves it dramatically. Besides, we apply the proposed deep feature weighting to some state-of-the-art naive Bayes text classifiers and have achieved remarkable improvements.},
   author = {Liangxiao Jiang and Chaoqun Li and Shasha Wang and Lungan Zhang},
   doi = {10.1016/J.ENGAPPAI.2016.02.002},
   issn = {0952-1976},
   journal = {Engineering Applications of Artificial Intelligence},
   keywords = {Correlation-based feature selection,Feature weighting,Naive Bayes,Text classification},
   month = {6},
   pages = {26-39},
   publisher = {Pergamon},
   title = {Deep feature weighting for naive Bayes and its application to text classification},
   volume = {52},
   url = {https://www.sciencedirect.com/science/article/abs/pii/S0952197616300112?via%3Dihub},
   year = {2016}
}


@InProceedings{10.1007/3-540-45683-X_45,
author="Kim, Sang-Bum
and Rim, Hae-Chang
and Yook, DongSuk
and Lim, Heui-Seok",
editor="Ishizuka, Mitsuru
and Sattar, Abdul",
title="Effective Methods for Improving Naive Bayes Text Classifiers",
booktitle="PRICAI 2002: Trends in Artificial Intelligence",
year="2002",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="414--423",
abstract="Though naive Bayes text classifiers are widely used because of its simplicity, the techniques for improving performances of these classifiers have been rarely studied. In this paper, we propose and evaluate some general and effective techniques for improving performance of the naive Bayes text classifier. We suggest document model based parameter estimation and document length normalization to alleviate the problems in the traditional multinomial approach for text classification. In addition, Mutual-Information-weighted naive Bayes text classifier is proposed to increase the effect of highly informative words. Our techniques are evaluated on the Reuters21578 and 20 Newsgroups collections, and significant improvements are obtained over the existing multinomial naive Bayes approach.",
isbn="978-3-540-45683-4",
doi = {https://doi.org/10.1007/3-540-45683-X_45}
}

@InProceedings{10.1007/978-3-540-30586-6_76,
author="Schneider, Karl-Michael",
editor="Gelbukh, Alexander",
title="Techniques for Improving the Performance of Naive Bayes for Text Classification",
booktitle="Computational Linguistics and Intelligent Text Processing",
year="2005",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="682--693",
abstract="Naive Bayes is often used in text classification applications and experiments because of its simplicity and effectiveness. However, its performance is often degraded because it does not model text well, and by inappropriate feature selection and the lack of reliable confidence scores. We address these problems and show that they can be solved by some simple corrections. We demonstrate that our simple modifications are able to improve the performance of Naive Bayes for text classification significantly.",
isbn="978-3-540-30586-6",
doi = {https://doi.org/10.1007/978-3-540-30586-6_76}
}

@InProceedings{10.1007/978-3-540-71496-5_73,
author="He, Feng
and Ding, Xiaoqing",
editor="Amati, Giambattista
and Carpineto, Claudio
and Romano, Giovanni",
title="Improving Naive Bayes Text Classifier Using Smoothing Methods",
booktitle="Advances in Information Retrieval",
year="2007",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="703--707",
abstract="The performance of naive Bayes text classifier is greatly influenced by parameter estimation, while the large vocabulary and scarce labeled training set bring difficulty in parameter estimation. In this paper, several smoothing methods are introduced to estimate parameters in naive Bayes text classifier. The proposed approaches can achieve better and more stable performance than Laplace smoothing.",
isbn="978-3-540-71496-5",
doi = {https://doi.org/10.1007/978-3-540-71496-5_73}
}

@article{FENG2015109,
title = {Feature subset selection using naive Bayes for text classification},
journal = {Pattern Recognition Letters},
volume = {65},
pages = {109-115},
year = {2015},
issn = {0167-8655},
doi = {https://doi.org/10.1016/j.patrec.2015.07.028},
url = {https://www.sciencedirect.com/science/article/pii/S0167865515002378},
author = {Guozhong Feng and Jianhua Guo and Bing-Yi Jing and Tieli Sun},
keywords = {Bayesian model averaging, Global selection index, Latent selection augmented naive Bayes, Local selection index, Text classification},
abstract = {Feature subset selection is known to improve text classification performance of various classifiers. The model using the selected features is often regarded as if it had generated the data. By taking its uncertainty into account, the discrimination capabilities can be measured by a global selection index (GSI), which can be used in the prediction function. In this paper, we propose a latent selection augmented naive (LSAN) Bayes classifier. By introducing a latent feature selection indicator, the GSI can be factorized into each local selection index (LSI). Using conjugate priors, the LSI for feature evaluation can be explicitly calculated. Then the feature subset selection models can be pruned by thresholding the LSIs, and the LSAN classifier can be achieved by the product of a small percentage of single feature model averages. The numerical results on some real datasets show that the proposed method outperforms the contrast feature weighting methods, and is very competitive if compared with some other commonly used classifiers such as SVM.}
}

@InProceedings{10.1007/11735106_17,
author="Yin, Ling
and Power, Richard",
editor="Lalmas, Mounia
and MacFarlane, Andy
and R{\"u}ger, Stefan
and Tombros, Anastasios
and Tsikrika, Theodora
and Yavlinsky, Alexei",
title="Adapting the Naive Bayes Classifier to Rank Procedural Texts",
booktitle="Advances in Information Retrieval",
year="2006",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="179--190",
abstract="This paper presents a machine-learning approach for ranking web documents according to the proportion of procedural text they contain. By `procedural text' we refer to ordered lists of steps, which are very common in some instructional genres such as online manuals. Our initial training corpus is built up by applying some simple heuristics to select documents from a large collection and contains only a few documents with a large proportion of procedural texts. We adapt the Naive Bayes classifier to better fit this less than ideal training corpus. This adapted model is compared with several other classifiers in ranking procedural texts using different sets of features and is shown to perform well when only highly distinctive features are used.",
isbn="978-3-540-33348-7",
doi = {https://doi.org/10.1007/11735106_17}
}

@article{CHEN20095432,
title = {Feature selection for text classification with Naïve Bayes},
journal = {Expert Systems with Applications},
volume = {36},
number = {3, Part 1},
pages = {5432-5435},
year = {2009},
issn = {0957-4174},
doi = {https://doi.org/10.1016/j.eswa.2008.06.054},
url = {https://www.sciencedirect.com/science/article/pii/S0957417408003564},
author = {Jingnian Chen and Houkuan Huang and Shengfeng Tian and Youli Qu},
keywords = {Text classification, Feature selection, Text preprocessing, Naïve Bayes},
abstract = {As an important preprocessing technology in text classification, feature selection can improve the scalability, efficiency and accuracy of a text classifier. In general, a good feature selection method should consider domain and algorithm characteristics. As the Naïve Bayesian classifier is very simple and efficient and highly sensitive to feature selection, so the research of feature selection specially for it is significant. This paper presents two feature evaluation metrics for the Naïve Bayesian classifier applied on multi-class text datasets: Multi-class Odds Ratio (MOR), and Class Discriminating Measure (CDM). Experiments of text classification with Naïve Bayesian classifiers were carried out on two multi-class texts collections. As the results indicate, CDM and MOR gain obviously better selecting effect than other feature selection approaches.}
}

@article{ZHANG20112160,
title = {An Improvement to Naive Bayes for Text Classification},
journal = {Procedia Engineering},
volume = {15},
pages = {2160-2164},
year = {2011},
note = {CEIS 2011},
issn = {1877-7058},
doi = {https://doi.org/10.1016/j.proeng.2011.08.404},
url = {https://www.sciencedirect.com/science/article/pii/S1877705811019059},
author = {Wei Zhang and Feng Gao},
keywords = {Text classification, Feature selection, Machine learning, Naïve Bayes},
abstract = {Naïve Bayes classifiers which are widely used for text classification in machine learning are based on the conditional probability of features belonging to a class, which the features are selected by feature selection methods. In this paper, an auxiliary feature method is proposed. It determines features by an existing feature selection method, and selects an auxiliary feature which can reclassify the text space aimed at the chosen features. Then the corresponding conditional probability is adjusted in order to improve classification accuracy. Illustrative examples show that the proposed meth-od indeed improves the performance of naïve Bayes classifier.}
}

@article{FENG2015109,
title = {Feature subset selection using naive Bayes for text classification},
journal = {Pattern Recognition Letters},
volume = {65},
pages = {109-115},
year = {2015},
issn = {0167-8655},
doi = {https://doi.org/10.1016/j.patrec.2015.07.028},
url = {https://www.sciencedirect.com/science/article/pii/S0167865515002378},
author = {Guozhong Feng and Jianhua Guo and Bing-Yi Jing and Tieli Sun},
keywords = {Bayesian model averaging, Global selection index, Latent selection augmented naive Bayes, Local selection index, Text classification},
abstract = {Feature subset selection is known to improve text classification performance of various classifiers. The model using the selected features is often regarded as if it had generated the data. By taking its uncertainty into account, the discrimination capabilities can be measured by a global selection index (GSI), which can be used in the prediction function. In this paper, we propose a latent selection augmented naive (LSAN) Bayes classifier. By introducing a latent feature selection indicator, the GSI can be factorized into each local selection index (LSI). Using conjugate priors, the LSI for feature evaluation can be explicitly calculated. Then the feature subset selection models can be pruned by thresholding the LSIs, and the LSAN classifier can be achieved by the product of a small percentage of single feature model averages. The numerical results on some real datasets show that the proposed method outperforms the contrast feature weighting methods, and is very competitive if compared with some other commonly used classifiers such as SVM.}
}

@article{YOUN2009477,
title = {Class dependent feature scaling method using naive Bayes classifier for text datamining},
journal = {Pattern Recognition Letters},
volume = {30},
number = {5},
pages = {477-485},
year = {2009},
issn = {0167-8655},
doi = {https://doi.org/10.1016/j.patrec.2008.11.013},
url = {https://www.sciencedirect.com/science/article/pii/S0167865508003553},
author = {Eunseog Youn and Myong K. Jeong},
keywords = {Classification, Feature selection, Naive Bayes classifier, Recursive feature elimination},
abstract = {The problem of feature selection is to find a subset of features for optimal classification. A critical part of feature selection is to rank features according to their importance for classification. The naive Bayes classifier has been extensively used in text categorization. We have developed a new feature scaling method, called class–dependent–feature–weighting (CDFW) using naive Bayes (NB) classifier. A new feature scaling method, CDFW–NB–RFE, combines CDFW and recursive feature elimination (RFE). Our experimental results showed that CDFW–NB–RFE outperformed other popular feature ranking schemes used on text datasets.}
}

@article{ZHANG2016137,
title = {Two feature weighting approaches for naive Bayes text classifiers},
journal = {Knowledge-Based Systems},
volume = {100},
pages = {137-144},
year = {2016},
issn = {0950-7051},
doi = {https://doi.org/10.1016/j.knosys.2016.02.017},
url = {https://www.sciencedirect.com/science/article/pii/S0950705116001039},
author = {Lungan Zhang and Liangxiao Jiang and Chaoqun Li and Ganggang Kong},
keywords = {Naive Bayes text classifiers, Feature weighting, Gain ratio, Decision tree},
abstract = {This paper works on feature weighting approaches for naive Bayes text classifiers. Almost all existing feature weighting approaches for naive Bayes text classifiers have some defects: limited improvement to classification performance of naive Bayes text classifiers or sacrificing the simplicity and execution time of the final models. In fact, feature weighting is not new for machine learning community, and many researchers have made fruitful efforts in the field of feature weighting. This paper reviews some simple and efficient feature weighting approaches designed for standard naive Bayes classifiers, and adapts them for naive Bayes text classifiers. As a result, this paper proposes two adaptive feature weighting approaches for naive Bayes text classifiers. Experimental results based on benchmark and real-world data show that, compared to their competitors, our feature weighting approaches show higher classification accuracy, yet at the same time maintain the simplicity and lower execution time of the final models.}
}

@article{JIANG201626,
title = {Deep feature weighting for naive Bayes and its application to text classification},
journal = {Engineering Applications of Artificial Intelligence},
volume = {52},
pages = {26-39},
year = {2016},
issn = {0952-1976},
doi = {https://doi.org/10.1016/j.engappai.2016.02.002},
url = {https://www.sciencedirect.com/science/article/pii/S0952197616300112},
author = {Liangxiao Jiang and Chaoqun Li and Shasha Wang and Lungan Zhang},
keywords = {Naive Bayes, Feature weighting, Correlation-based feature selection, Text classification},
abstract = {Naive Bayes (NB) continues to be one of the top 10 data mining algorithms due to its simplicity, efficiency and efficacy. Of numerous proposals to improve the accuracy of naive Bayes by weakening its feature independence assumption, the feature weighting approach has received less attention from researchers. Moreover, to our knowledge, all of the existing feature weighting approaches only incorporate the learned feature weights into the classification of formula of naive Bayes and do not incorporate the learned feature weights into its conditional probability estimates at all. In this paper, we propose a simple, efficient, and effective feature weighting approach, called deep feature weighting (DFW), which estimates the conditional probabilities of naive Bayes by deeply computing feature weighted frequencies from training data. Empirical studies on a collection of 36 benchmark datasets from the UCI repository show that naive Bayes with deep feature weighting rarely degrades the quality of the model compared to standard naive Bayes and, in many cases, improves it dramatically. Besides, we apply the proposed deep feature weighting to some state-of-the-art naive Bayes text classifiers and have achieved remarkable improvements.}
}

@article{ELHINDI2020106652,
title = {Lazy fine-tuning algorithms for naïve Bayesian text classification},
journal = {Applied Soft Computing},
volume = {96},
pages = {106652},
year = {2020},
issn = {1568-4946},
doi = {https://doi.org/10.1016/j.asoc.2020.106652},
url = {https://www.sciencedirect.com/science/article/pii/S1568494620305901},
author = {Khalil M. {El Hindi} and Reem R. Aljulaidan and Hussien AlSalman},
keywords = {Fine-tuning Naïve Bayes, Document categorization, Local learning, Multinomial text classification, Complement NB, One-versus-all NB},
abstract = {The naïve Bayes (NB) learning algorithm is widely applied in many fields, particularly in text classification. However, its performance decreases when it is used in domains where its naïve assumption is violated or when the training set is too small to find accurate estimations of the probabilities. In this study, we propose a lazy fine-tuning naïve Bayes (LFTNB) method to address both problems. We propose a local fine-tuning algorithm that uses the nearest neighbors of a query instance to fine-tune the probability terms used by NB. Applying the nearest neighbors only makes the independence assumption more likely to be valid, whereas the fine-tuning algorithm is used to find more accurate estimations of the probability terms. The performance of the LFTNB approach was evaluated using 47 UCI datasets. The results show that the LFTNB method achieves superior performance than classical NB, eager FTNB, and k-nearest neighbor algorithms. We also propose eager and lazy fine-tuning versions of powerful NB-based text classification algorithms, namely, multinomial NB, complement NB, and one-versus-all NB. The empirical results using 18 UCI text classification datasets show that the proposed methods outperform untuned versions of these algorithms.}
}

@article{LU2010598,
title = {Chinese text classification by the Naïve Bayes Classifier and the associative classifier with multiple confidence threshold values},
journal = {Knowledge-Based Systems},
volume = {23},
number = {6},
pages = {598-604},
year = {2010},
issn = {0950-7051},
doi = {https://doi.org/10.1016/j.knosys.2010.04.004},
url = {https://www.sciencedirect.com/science/article/pii/S0950705110000638},
author = {Shing-Hwa Lu and Ding-An Chiang and Huan-Chao Keh and Hui-Hua Huang},
keywords = {Association classification, Text classification, Text mining, Text categorization},
abstract = {Each type of classifier has its own advantages as well as certain shortcomings. In this paper, we take the advantages of the associative classifier and the Naïve Bayes Classifier to make up the shortcomings of each other, thus improving the accuracy of text classification. We will classify the training cases with the Naïve Bayes Classifier and set different confidence threshold values for different class association rules (CARs) to different classes by the obtained classification accuracy rate of the Naïve Bayes Classifier to the classes. Since the accuracy rates of all selected CARs of the class are higher than that obtained by the Naïve Bayes Classifier, we could further optimize the classification result through these selected CARs. Moreover, for those unclassified cases, we will classify them with the Naïve Bayes Classifier. The experimental results show that combining the advantages of these two different classifiers better classification result can be obtained than with a single classifier.}
}

@article{KIM2018128,
title = {Towards perfect text classification with Wikipedia-based semantic Naïve Bayes learning},
journal = {Neurocomputing},
volume = {315},
pages = {128-134},
year = {2018},
issn = {0925-2312},
doi = {https://doi.org/10.1016/j.neucom.2018.07.002},
url = {https://www.sciencedirect.com/science/article/pii/S0925231218308282},
author = {Han-joon Kim and Jiyun Kim and Jinseog Kim and Pureum Lim},
keywords = {Text classification, Naïve Bayes learning, Tensor space, Wikipedia, Semantic features},
abstract = {This paper suggests a novel way of dramatically improving the Naïve Bayes text classifier with our semantic tensor space model for document representation. In our work, we intend to achieve a perfect text classification with the semantic Naïve Bayes learning that incorporates the semantic concept features into term feature statistics; for this, the Naïve Bayes learning is semantically augmented under the tensor space model where the ‘concept’ space is regarded as an independent space equated with the ‘term’ and ‘document’ spaces, and it is produced with concept-level informative Wikipedia pages associated with a given document corpus. Through extensive experiments using three popular document corpora including Reuters-21578, 20Newsgroups, and OHSUMED corpora, we prove that the proposed method not only has superiority over the recent deep learning-based classification methods but also shows nearly perfect classification performance.}
}

@inproceedings{10.5555/1619645.1619732,
author = {Dai, Wenyuan and Xue, Gui-Rong and Yang, Qiang and Yu, Yong},
title = {Transferring naive bayes classifiers for text classification},
year = {2007},
isbn = {9781577353232},
publisher = {AAAI Press},
abstract = {A basic assumption in traditional machine learning is that the training and test data distributions should be identical. This assumption may not hold in many situations in practice, but we may be forced to rely on a different-distribution data to learn a prediction model. For example, this may be the case when it is expensive to label the data in a domain of interest, although in a related but different domain there may be plenty of labeled data available. In this paper, we propose a novel transfer-learning algorithm for text classification based on an EM-based Naive Bayes classifiers. Our solution is to first estimate the initial probabilities under a distribution Dl of one labeled data set, and then use an EM algorithm to revise the model for a different distribution Du of the test data which are unlabeled. We show that our algorithm is very effective in several different pairs of domains, where the distances between the different distributions are measured using the Kullback-Leibler (KL) divergence. Moreover, KL-divergence is used to decide the trade-off parameters in our algorithm. In the experiment, our algorithm outperforms the traditional supervised and semi-supervised learning algorithms when the distributions of the training and test sets are increasingly different.},
booktitle = {Proceedings of the 22nd National Conference on Artificial Intelligence - Volume 1},
pages = {540–545},
numpages = {6},
location = {Vancouver, British Columbia, Canada},
series = {AAAI'07},
url = {https://dl.acm.org/doi/10.5555/1619645.1619732}
}
```

# prompt6
Mira si no tengo ningun duplicado:
```bibtex
@article{Kim2006,
   abstract = {While naive Bayes is quite effective in various data mining tasks, it shows a disappointing result in the automatic text classification problem. Based on the observation of naive Bayes for the natural language text, we found a serious problem in the parameter estimation process, which causes poor results in text classification domain. In this paper, we propose two empirical heuristics: per-document text normalization and feature weighting method. While these are somewhat ad hoc methods, our proposed naive Bayes text classifier performs very well in the standard benchmark collections, competing with state-of-the-art text classifiers based on a highly complex learning method such as SVM. © 2006, IEEE. All rights reserved.},
   author = {Sang Bum Kim and Kyoung Soo Han and Hae Chang Rim and Sung Hyon Myaeng},
   doi = {10.1109/TKDE.2006.180},
   issn = {10414347},
   issue = {11},
   journal = {IEEE Transactions on Knowledge and Data Engineering},
   keywords = {Poisson model,Text classification,feature weighting,naive Bayes classifier},
   month = {11},
   pages = {1457-1466},
   title = {Some effective techniques for naive bayes text classification},
   volume = {18},
   url = {https://ieeexplore.ieee.org/document/1704799},
   year = {2006}
}
@article{Sangounpao2019,
   abstract = {Content less than two hundred words like comments or review statements is known as a short text. Short text classification is useful for automatically categorizing sentence into predefined group. There are several traditional short text classification methods by using bag-of-words with k nearest neighbors (k-NN), Naïve Bayes, Maximum entropy, support vector machines (SVMs), and an algorithm based on statistics and rules. The deep learning method is outperformed other methods on classification of short text with normal size of dataset. Some researches classify requirements into functional and nonfunctional requirements. There is no research on multi-classification of functional requirements with a small dataset particularly for an accounting field. This paper presents an approach to classify short text for a small dataset into multiple categories of functional requirements on the accounting domain. The proposed approach uses an ontology to construct bag-of-words and uses Naive Bayes to classify for small dataset. The experiment is conducted using four hundred of datasets with 5folds and 10-folds cross-validation. The result shows that the method can correctly classify more than 80%. Additionally, comparisons between the ontology-based Naive Bayes method and other methods are investigated.},
   author = {Ketkaew Sangounpao and Pornsiri Muenchaisri},
   doi = {10.1109/SNPD.2019.8935711},
   isbn = {9781728116518},
   journal = {Proceedings - 20th IEEE/ACIS International Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing, SNPD 2019},
   keywords = {accounting domain knowledge,multi-classification,ontology,requirements engineering,short text classification,small dataset,traditional classification},
   month = {7},
   pages = {53-58},
   publisher = {Institute of Electrical and Electronics Engineers Inc.},
   title = {Ontology-Based Naive Bayes Short Text Classification Method for a Small Dataset},
   url = {https://ieeexplore.ieee.org/document/8935711},
   year = {2019}
}
@article{Frank2006,
   abstract = {Multinomial naive Bayes (MNB) is a popular method for document classification due to its computational efficiency and relatively good predictive performance. It has recently been established that predictive performance can be improved further by appropriate data...},
   author = {Eibe Frank and Remco R. Bouckaert},
   doi = {10.1007/11871637_49},
   isbn = {978-3-540-46048-0},
   issn = {1611-3349},
   journal = {Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)},
   pages = {503-510},
   publisher = {Springer, Berlin, Heidelberg},
   title = {Naive Bayes for Text Classification with Unbalanced Classes},
   volume = {4213 LNAI},
   url = {https://link.springer.com/chapter/10.1007/11871637_49},
   year = {2006}
}
@inproceedings{10.1145/2911451.2911547,
author = {Zhang, Dell and Wang, Jun and Yilmaz, Emine and Wang, Xiaoling and Zhou, Yuxin},
title = {Bayesian Performance Comparison of Text Classifiers},
year = {2016},
isbn = {9781450340694},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/2911451.2911547},
doi = {10.1145/2911451.2911547},
abstract = {How can we know whether one classifier is really better than the other? In the area of text classification, since the publication of Yang and Liu's seminal SIGIR-1999 paper, it has become a standard practice for researchers to apply null-hypothesis significance testing (NHST) on their experimental results in order to establish the superiority of a classifier. However, such a frequentist approach has a number of inherent deficiencies and limitations, e.g., the inability to accept the null hypothesis (that the two classifiers perform equally well), the difficulty to compare commonly-used multivariate performance measures like F1 scores instead of accuracy, and so on. In this paper, we propose a novel Bayesian approach to the performance comparison of text classifiers, and argue its advantages over the traditional frequentist approach based on t-test etc. In contrast to the existing probabilistic model for F1 scores which is unpaired, our proposed model takes the correlation between classifiers into account and thus achieves greater statistical power. Using several typical text classification algorithms and a benchmark dataset, we demonstrate that the our approach provides rich information about the difference between two classifiers' performances.},
booktitle = {Proceedings of the 39th International ACM SIGIR Conference on Research and Development in Information Retrieval},
pages = {15–24},
numpages = {10},
keywords = {bayesian inference, hypothesis testing, performance evaluation, text classification},
location = {Pisa, Italy},
series = {SIGIR '16}
}
@article{Jiang2016,
   abstract = {Naive Bayes (NB) continues to be one of the top 10 data mining algorithms due to its simplicity, efficiency and efficacy. Of numerous proposals to improve the accuracy of naive Bayes by weakening its feature independence assumption, the feature weighting approach has received less attention from researchers. Moreover, to our knowledge, all of the existing feature weighting approaches only incorporate the learned feature weights into the classification of formula of naive Bayes and do not incorporate the learned feature weights into its conditional probability estimates at all. In this paper, we propose a simple, efficient, and effective feature weighting approach, called deep feature weighting (DFW), which estimates the conditional probabilities of naive Bayes by deeply computing feature weighted frequencies from training data. Empirical studies on a collection of 36 benchmark datasets from the UCI repository show that naive Bayes with deep feature weighting rarely degrades the quality of the model compared to standard naive Bayes and, in many cases, improves it dramatically. Besides, we apply the proposed deep feature weighting to some state-of-the-art naive Bayes text classifiers and have achieved remarkable improvements.},
   author = {Liangxiao Jiang and Chaoqun Li and Shasha Wang and Lungan Zhang},
   doi = {10.1016/J.ENGAPPAI.2016.02.002},
   issn = {0952-1976},
   journal = {Engineering Applications of Artificial Intelligence},
   keywords = {Correlation-based feature selection,Feature weighting,Naive Bayes,Text classification},
   month = {6},
   pages = {26-39},
   publisher = {Pergamon},
   title = {Deep feature weighting for naive Bayes and its application to text classification},
   volume = {52},
   url = {https://www.sciencedirect.com/science/article/abs/pii/S0952197616300112?via%3Dihub},
   year = {2016}
}
@InProceedings{10.1007/3-540-45683-X_45,
author="Kim, Sang-Bum
and Rim, Hae-Chang
and Yook, DongSuk
and Lim, Heui-Seok",
editor="Ishizuka, Mitsuru
and Sattar, Abdul",
title="Effective Methods for Improving Naive Bayes Text Classifiers",
booktitle="PRICAI 2002: Trends in Artificial Intelligence",
year="2002",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="414--423",
abstract="Though naive Bayes text classifiers are widely used because of its simplicity, the techniques for improving performances of these classifiers have been rarely studied. In this paper, we propose and evaluate some general and effective techniques for improving performance of the naive Bayes text classifier. We suggest document model based parameter estimation and document length normalization to alleviate the problems in the traditional multinomial approach for text classification. In addition, Mutual-Information-weighted naive Bayes text classifier is proposed to increase the effect of highly informative words. Our techniques are evaluated on the Reuters21578 and 20 Newsgroups collections, and significant improvements are obtained over the existing multinomial naive Bayes approach.",
isbn="978-3-540-45683-4",
doi = {https://doi.org/10.1007/3-540-45683-X_45}
}

@InProceedings{10.1007/978-3-540-30586-6_76,
author="Schneider, Karl-Michael",
editor="Gelbukh, Alexander",
title="Techniques for Improving the Performance of Naive Bayes for Text Classification",
booktitle="Computational Linguistics and Intelligent Text Processing",
year="2005",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="682--693",
abstract="Naive Bayes is often used in text classification applications and experiments because of its simplicity and effectiveness. However, its performance is often degraded because it does not model text well, and by inappropriate feature selection and the lack of reliable confidence scores. We address these problems and show that they can be solved by some simple corrections. We demonstrate that our simple modifications are able to improve the performance of Naive Bayes for text classification significantly.",
isbn="978-3-540-30586-6",
doi = {https://doi.org/10.1007/978-3-540-30586-6_76}
}

@InProceedings{10.1007/978-3-540-71496-5_73,
author="He, Feng
and Ding, Xiaoqing",
editor="Amati, Giambattista
and Carpineto, Claudio
and Romano, Giovanni",
title="Improving Naive Bayes Text Classifier Using Smoothing Methods",
booktitle="Advances in Information Retrieval",
year="2007",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="703--707",
abstract="The performance of naive Bayes text classifier is greatly influenced by parameter estimation, while the large vocabulary and scarce labeled training set bring difficulty in parameter estimation. In this paper, several smoothing methods are introduced to estimate parameters in naive Bayes text classifier. The proposed approaches can achieve better and more stable performance than Laplace smoothing.",
isbn="978-3-540-71496-5",
doi = {https://doi.org/10.1007/978-3-540-71496-5_73}
}

@InProceedings{10.1007/978-3-540-30549-1_43,
author="Kibriya, Ashraf M.
and Frank, Eibe
and Pfahringer, Bernhard
and Holmes, Geoffrey",
editor="Webb, Geoffrey I.
and Yu, Xinghuo",
title="Multinomial Naive Bayes for Text Categorization Revisited",
booktitle="AI 2004: Advances in Artificial Intelligence",
year="2005",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="488--499",
abstract="This paper presents empirical results for several versions of the multinomial naive Bayes classifier on four text categorization problems, and a way of improving it using locally weighted learning. More specifically, it compares standard multinomial naive Bayes to the recently proposed transformed weight-normalized complement naive Bayes classifier (TWCNB) [1], and shows that some of the modifications included in TWCNB may not be necessary to achieve optimum performance on some datasets. However, it does show that TFIDF conversion and document length normalization are important. It also shows that support vector machines can, in fact, sometimes very significantly outperform both methods. Finally, it shows how the performance of multinomial naive Bayes can be improved using locally weighted learning. However, the overall conclusion of our paper is that support vector machines are still the method of choice if the aim is to maximize accuracy.",
isbn="978-3-540-30549-1",
doi = {https://doi.org/10.1007/978-3-540-30549-1_43}
}

@InProceedings{10.1007/11735106_17,
author="Yin, Ling
and Power, Richard",
editor="Lalmas, Mounia
and MacFarlane, Andy
and R{\"u}ger, Stefan
and Tombros, Anastasios
and Tsikrika, Theodora
and Yavlinsky, Alexei",
title="Adapting the Naive Bayes Classifier to Rank Procedural Texts",
booktitle="Advances in Information Retrieval",
year="2006",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="179--190",
abstract="This paper presents a machine-learning approach for ranking web documents according to the proportion of procedural text they contain. By `procedural text' we refer to ordered lists of steps, which are very common in some instructional genres such as online manuals. Our initial training corpus is built up by applying some simple heuristics to select documents from a large collection and contains only a few documents with a large proportion of procedural texts. We adapt the Naive Bayes classifier to better fit this less than ideal training corpus. This adapted model is compared with several other classifiers in ranking procedural texts using different sets of features and is shown to perform well when only highly distinctive features are used.",
isbn="978-3-540-33348-7",
doi = {https://doi.org/10.1007/11735106_17}
}

@article{CHEN20095432,
title = {Feature selection for text classification with Naïve Bayes},
journal = {Expert Systems with Applications},
volume = {36},
number = {3, Part 1},
pages = {5432-5435},
year = {2009},
issn = {0957-4174},
doi = {https://doi.org/10.1016/j.eswa.2008.06.054},
url = {https://www.sciencedirect.com/science/article/pii/S0957417408003564},
author = {Jingnian Chen and Houkuan Huang and Shengfeng Tian and Youli Qu},
keywords = {Text classification, Feature selection, Text preprocessing, Naïve Bayes},
abstract = {As an important preprocessing technology in text classification, feature selection can improve the scalability, efficiency and accuracy of a text classifier. In general, a good feature selection method should consider domain and algorithm characteristics. As the Naïve Bayesian classifier is very simple and efficient and highly sensitive to feature selection, so the research of feature selection specially for it is significant. This paper presents two feature evaluation metrics for the Naïve Bayesian classifier applied on multi-class text datasets: Multi-class Odds Ratio (MOR), and Class Discriminating Measure (CDM). Experiments of text classification with Naïve Bayesian classifiers were carried out on two multi-class texts collections. As the results indicate, CDM and MOR gain obviously better selecting effect than other feature selection approaches.}
}

@article{ZHANG20112160,
title = {An Improvement to Naive Bayes for Text Classification},
journal = {Procedia Engineering},
volume = {15},
pages = {2160-2164},
year = {2011},
note = {CEIS 2011},
issn = {1877-7058},
doi = {https://doi.org/10.1016/j.proeng.2011.08.404},
url = {https://www.sciencedirect.com/science/article/pii/S1877705811019059},
author = {Wei Zhang and Feng Gao},
keywords = {Text classification, Feature selection, Machine learning, Naïve Bayes},
abstract = {Naïve Bayes classifiers which are widely used for text classification in machine learning are based on the conditional probability of features belonging to a class, which the features are selected by feature selection methods. In this paper, an auxiliary feature method is proposed. It determines features by an existing feature selection method, and selects an auxiliary feature which can reclassify the text space aimed at the chosen features. Then the corresponding conditional probability is adjusted in order to improve classification accuracy. Illustrative examples show that the proposed meth-od indeed improves the performance of naïve Bayes classifier.}
}

@article{FENG2015109,
title = {Feature subset selection using naive Bayes for text classification},
journal = {Pattern Recognition Letters},
volume = {65},
pages = {109-115},
year = {2015},
issn = {0167-8655},
doi = {https://doi.org/10.1016/j.patrec.2015.07.028},
url = {https://www.sciencedirect.com/science/article/pii/S0167865515002378},
author = {Guozhong Feng and Jianhua Guo and Bing-Yi Jing and Tieli Sun},
keywords = {Bayesian model averaging, Global selection index, Latent selection augmented naive Bayes, Local selection index, Text classification},
abstract = {Feature subset selection is known to improve text classification performance of various classifiers. The model using the selected features is often regarded as if it had generated the data. By taking its uncertainty into account, the discrimination capabilities can be measured by a global selection index (GSI), which can be used in the prediction function. In this paper, we propose a latent selection augmented naive (LSAN) Bayes classifier. By introducing a latent feature selection indicator, the GSI can be factorized into each local selection index (LSI). Using conjugate priors, the LSI for feature evaluation can be explicitly calculated. Then the feature subset selection models can be pruned by thresholding the LSIs, and the LSAN classifier can be achieved by the product of a small percentage of single feature model averages. The numerical results on some real datasets show that the proposed method outperforms the contrast feature weighting methods, and is very competitive if compared with some other commonly used classifiers such as SVM.}
}

@article{YOUN2009477,
title = {Class dependent feature scaling method using naive Bayes classifier for text datamining},
journal = {Pattern Recognition Letters},
volume = {30},
number = {5},
pages = {477-485},
year = {2009},
issn = {0167-8655},
doi = {https://doi.org/10.1016/j.patrec.2008.11.013},
url = {https://www.sciencedirect.com/science/article/pii/S0167865508003553},
author = {Eunseog Youn and Myong K. Jeong},
keywords = {Classification, Feature selection, Naive Bayes classifier, Recursive feature elimination},
abstract = {The problem of feature selection is to find a subset of features for optimal classification. A critical part of feature selection is to rank features according to their importance for classification. The naive Bayes classifier has been extensively used in text categorization. We have developed a new feature scaling method, called class–dependent–feature–weighting (CDFW) using naive Bayes (NB) classifier. A new feature scaling method, CDFW–NB–RFE, combines CDFW and recursive feature elimination (RFE). Our experimental results showed that CDFW–NB–RFE outperformed other popular feature ranking schemes used on text datasets.}
}

@article{ZHANG2016137,
title = {Two feature weighting approaches for naive Bayes text classifiers},
journal = {Knowledge-Based Systems},
volume = {100},
pages = {137-144},
year = {2016},
issn = {0950-7051},
doi = {https://doi.org/10.1016/j.knosys.2016.02.017},
url = {https://www.sciencedirect.com/science/article/pii/S0950705116001039},
author = {Lungan Zhang and Liangxiao Jiang and Chaoqun Li and Ganggang Kong},
keywords = {Naive Bayes text classifiers, Feature weighting, Gain ratio, Decision tree},
abstract = {This paper works on feature weighting approaches for naive Bayes text classifiers. Almost all existing feature weighting approaches for naive Bayes text classifiers have some defects: limited improvement to classification performance of naive Bayes text classifiers or sacrificing the simplicity and execution time of the final models. In fact, feature weighting is not new for machine learning community, and many researchers have made fruitful efforts in the field of feature weighting. This paper reviews some simple and efficient feature weighting approaches designed for standard naive Bayes classifiers, and adapts them for naive Bayes text classifiers. As a result, this paper proposes two adaptive feature weighting approaches for naive Bayes text classifiers. Experimental results based on benchmark and real-world data show that, compared to their competitors, our feature weighting approaches show higher classification accuracy, yet at the same time maintain the simplicity and lower execution time of the final models.}
}

@article{JIANG201626,
title = {Deep feature weighting for naive Bayes and its application to text classification},
journal = {Engineering Applications of Artificial Intelligence},
volume = {52},
pages = {26-39},
year = {2016},
issn = {0952-1976},
doi = {https://doi.org/10.1016/j.engappai.2016.02.002},
url = {https://www.sciencedirect.com/science/article/pii/S0952197616300112},
author = {Liangxiao Jiang and Chaoqun Li and Shasha Wang and Lungan Zhang},
keywords = {Naive Bayes, Feature weighting, Correlation-based feature selection, Text classification},
abstract = {Naive Bayes (NB) continues to be one of the top 10 data mining algorithms due to its simplicity, efficiency and efficacy. Of numerous proposals to improve the accuracy of naive Bayes by weakening its feature independence assumption, the feature weighting approach has received less attention from researchers. Moreover, to our knowledge, all of the existing feature weighting approaches only incorporate the learned feature weights into the classification of formula of naive Bayes and do not incorporate the learned feature weights into its conditional probability estimates at all. In this paper, we propose a simple, efficient, and effective feature weighting approach, called deep feature weighting (DFW), which estimates the conditional probabilities of naive Bayes by deeply computing feature weighted frequencies from training data. Empirical studies on a collection of 36 benchmark datasets from the UCI repository show that naive Bayes with deep feature weighting rarely degrades the quality of the model compared to standard naive Bayes and, in many cases, improves it dramatically. Besides, we apply the proposed deep feature weighting to some state-of-the-art naive Bayes text classifiers and have achieved remarkable improvements.}
}

@article{ELHINDI2020106652,
title = {Lazy fine-tuning algorithms for naïve Bayesian text classification},
journal = {Applied Soft Computing},
volume = {96},
pages = {106652},
year = {2020},
issn = {1568-4946},
doi = {https://doi.org/10.1016/j.asoc.2020.106652},
url = {https://www.sciencedirect.com/science/article/pii/S1568494620305901},
author = {Khalil M. {El Hindi} and Reem R. Aljulaidan and Hussien AlSalman},
keywords = {Fine-tuning Naïve Bayes, Document categorization, Local learning, Multinomial text classification, Complement NB, One-versus-all NB},
abstract = {The naïve Bayes (NB) learning algorithm is widely applied in many fields, particularly in text classification. However, its performance decreases when it is used in domains where its naïve assumption is violated or when the training set is too small to find accurate estimations of the probabilities. In this study, we propose a lazy fine-tuning naïve Bayes (LFTNB) method to address both problems. We propose a local fine-tuning algorithm that uses the nearest neighbors of a query instance to fine-tune the probability terms used by NB. Applying the nearest neighbors only makes the independence assumption more likely to be valid, whereas the fine-tuning algorithm is used to find more accurate estimations of the probability terms. The performance of the LFTNB approach was evaluated using 47 UCI datasets. The results show that the LFTNB method achieves superior performance than classical NB, eager FTNB, and k-nearest neighbor algorithms. We also propose eager and lazy fine-tuning versions of powerful NB-based text classification algorithms, namely, multinomial NB, complement NB, and one-versus-all NB. The empirical results using 18 UCI text classification datasets show that the proposed methods outperform untuned versions of these algorithms.}
}

@article{LU2010598,
title = {Chinese text classification by the Naïve Bayes Classifier and the associative classifier with multiple confidence threshold values},
journal = {Knowledge-Based Systems},
volume = {23},
number = {6},
pages = {598-604},
year = {2010},
issn = {0950-7051},
doi = {https://doi.org/10.1016/j.knosys.2010.04.004},
url = {https://www.sciencedirect.com/science/article/pii/S0950705110000638},
author = {Shing-Hwa Lu and Ding-An Chiang and Huan-Chao Keh and Hui-Hua Huang},
keywords = {Association classification, Text classification, Text mining, Text categorization},
abstract = {Each type of classifier has its own advantages as well as certain shortcomings. In this paper, we take the advantages of the associative classifier and the Naïve Bayes Classifier to make up the shortcomings of each other, thus improving the accuracy of text classification. We will classify the training cases with the Naïve Bayes Classifier and set different confidence threshold values for different class association rules (CARs) to different classes by the obtained classification accuracy rate of the Naïve Bayes Classifier to the classes. Since the accuracy rates of all selected CARs of the class are higher than that obtained by the Naïve Bayes Classifier, we could further optimize the classification result through these selected CARs. Moreover, for those unclassified cases, we will classify them with the Naïve Bayes Classifier. The experimental results show that combining the advantages of these two different classifiers better classification result can be obtained than with a single classifier.}
}

@article{KIM2018128,
title = {Towards perfect text classification with Wikipedia-based semantic Naïve Bayes learning},
journal = {Neurocomputing},
volume = {315},
pages = {128-134},
year = {2018},
issn = {0925-2312},
doi = {https://doi.org/10.1016/j.neucom.2018.07.002},
url = {https://www.sciencedirect.com/science/article/pii/S0925231218308282},
author = {Han-joon Kim and Jiyun Kim and Jinseog Kim and Pureum Lim},
keywords = {Text classification, Naïve Bayes learning, Tensor space, Wikipedia, Semantic features},
abstract = {This paper suggests a novel way of dramatically improving the Naïve Bayes text classifier with our semantic tensor space model for document representation. In our work, we intend to achieve a perfect text classification with the semantic Naïve Bayes learning that incorporates the semantic concept features into term feature statistics; for this, the Naïve Bayes learning is semantically augmented under the tensor space model where the ‘concept’ space is regarded as an independent space equated with the ‘term’ and ‘document’ spaces, and it is produced with concept-level informative Wikipedia pages associated with a given document corpus. Through extensive experiments using three popular document corpora including Reuters-21578, 20Newsgroups, and OHSUMED corpora, we prove that the proposed method not only has superiority over the recent deep learning-based classification methods but also shows nearly perfect classification performance.}
}

@inproceedings{10.5555/1619645.1619732,
author = {Dai, Wenyuan and Xue, Gui-Rong and Yang, Qiang and Yu, Yong},
title = {Transferring naive bayes classifiers for text classification},
year = {2007},
isbn = {9781577353232},
publisher = {AAAI Press},
abstract = {A basic assumption in traditional machine learning is that the training and test data distributions should be identical. This assumption may not hold in many situations in practice, but we may be forced to rely on a different-distribution data to learn a prediction model. For example, this may be the case when it is expensive to label the data in a domain of interest, although in a related but different domain there may be plenty of labeled data available. In this paper, we propose a novel transfer-learning algorithm for text classification based on an EM-based Naive Bayes classifiers. Our solution is to first estimate the initial probabilities under a distribution Dl of one labeled data set, and then use an EM algorithm to revise the model for a different distribution Du of the test data which are unlabeled. We show that our algorithm is very effective in several different pairs of domains, where the distances between the different distributions are measured using the Kullback-Leibler (KL) divergence. Moreover, KL-divergence is used to decide the trade-off parameters in our algorithm. In the experiment, our algorithm outperforms the traditional supervised and semi-supervised learning algorithms when the distributions of the training and test sets are increasingly different.},
booktitle = {Proceedings of the 22nd National Conference on Artificial Intelligence - Volume 1},
pages = {540–545},
numpages = {6},
location = {Vancouver, British Columbia, Canada},
series = {AAAI'07},
url = {https://dl.acm.org/doi/10.5555/1619645.1619732}
}

@INPROCEEDINGS{4554061,
  author={Ding, Wang and Yu, Songnian and Wang, Qianfeng and Yu, Jiaqi and Guo, Qiang},
  booktitle={2008 International Symposiums on Information Processing}, 
  title={A Novel Naive Bayesian Text Classifier}, 
  year={2008},
  volume={},
  number={},
  pages={78-82},
  abstract={The naive Bayesian (NB) classifier is one of the simple but most efficient and stable classification methods. The great efficiency of NB is mainly because of the conditionally independence assumption among the attributes, which is problematic in practice especially while the attributes are strongly correlated. In this paper, we propose a novel NB text classifier, package and combined naive Bayesian text classifier (PC-NB) that relaxes the independence assumption. The main aim of PC-NB is to make naive Bayesian classifier be more accurate without efficiency reduction. A set of experiments were performed and the results of the analysis and experiment indicate that the proposed classifier is more accurate and powerful while the attributes of an instance are strongly correlated.},
  keywords={Bayesian methods;Text categorization;Niobium;Packaging;Artificial intelligence;Text mining;Information processing;Performance analysis;Support vector machines;Support vector machine classification;Text classification;Naive bayesian;Data mining},
  doi={10.1109/ISIP.2008.54},
  ISSN={},
  month={May},}

```

# prompt7
Completar la matriz bibliográfica con: autor(es), año, título, tipo de fuente, resumen del aporte, método usado, hallazgos clave.

Mi 20 artículos en formato bibtex:
```bibtex
@article{Kim2006,
   abstract = {While naive Bayes is quite effective in various data mining tasks, it shows a disappointing result in the automatic text classification problem. Based on the observation of naive Bayes for the natural language text, we found a serious problem in the parameter estimation process, which causes poor results in text classification domain. In this paper, we propose two empirical heuristics: per-document text normalization and feature weighting method. While these are somewhat ad hoc methods, our proposed naive Bayes text classifier performs very well in the standard benchmark collections, competing with state-of-the-art text classifiers based on a highly complex learning method such as SVM. © 2006, IEEE. All rights reserved.},
   author = {Sang Bum Kim and Kyoung Soo Han and Hae Chang Rim and Sung Hyon Myaeng},
   doi = {10.1109/TKDE.2006.180},
   issn = {10414347},
   issue = {11},
   journal = {IEEE Transactions on Knowledge and Data Engineering},
   keywords = {Poisson model,Text classification,feature weighting,naive Bayes classifier},
   month = {11},
   pages = {1457-1466},
   title = {Some effective techniques for naive bayes text classification},
   volume = {18},
   url = {https://ieeexplore.ieee.org/document/1704799},
   year = {2006}
}
@article{Sangounpao2019,
   abstract = {Content less than two hundred words like comments or review statements is known as a short text. Short text classification is useful for automatically categorizing sentence into predefined group. There are several traditional short text classification methods by using bag-of-words with k nearest neighbors (k-NN), Naïve Bayes, Maximum entropy, support vector machines (SVMs), and an algorithm based on statistics and rules. The deep learning method is outperformed other methods on classification of short text with normal size of dataset. Some researches classify requirements into functional and nonfunctional requirements. There is no research on multi-classification of functional requirements with a small dataset particularly for an accounting field. This paper presents an approach to classify short text for a small dataset into multiple categories of functional requirements on the accounting domain. The proposed approach uses an ontology to construct bag-of-words and uses Naive Bayes to classify for small dataset. The experiment is conducted using four hundred of datasets with 5folds and 10-folds cross-validation. The result shows that the method can correctly classify more than 80%. Additionally, comparisons between the ontology-based Naive Bayes method and other methods are investigated.},
   author = {Ketkaew Sangounpao and Pornsiri Muenchaisri},
   doi = {10.1109/SNPD.2019.8935711},
   isbn = {9781728116518},
   journal = {Proceedings - 20th IEEE/ACIS International Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing, SNPD 2019},
   keywords = {accounting domain knowledge,multi-classification,ontology,requirements engineering,short text classification,small dataset,traditional classification},
   month = {7},
   pages = {53-58},
   publisher = {Institute of Electrical and Electronics Engineers Inc.},
   title = {Ontology-Based Naive Bayes Short Text Classification Method for a Small Dataset},
   url = {https://ieeexplore.ieee.org/document/8935711},
   year = {2019}
}
@article{Frank2006,
   abstract = {Multinomial naive Bayes (MNB) is a popular method for document classification due to its computational efficiency and relatively good predictive performance. It has recently been established that predictive performance can be improved further by appropriate data...},
   author = {Eibe Frank and Remco R. Bouckaert},
   doi = {10.1007/11871637_49},
   isbn = {978-3-540-46048-0},
   issn = {1611-3349},
   journal = {Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)},
   pages = {503-510},
   publisher = {Springer, Berlin, Heidelberg},
   title = {Naive Bayes for Text Classification with Unbalanced Classes},
   volume = {4213 LNAI},
   url = {https://link.springer.com/chapter/10.1007/11871637_49},
   year = {2006}
}
@inproceedings{10.1145/2911451.2911547,
author = {Zhang, Dell and Wang, Jun and Yilmaz, Emine and Wang, Xiaoling and Zhou, Yuxin},
title = {Bayesian Performance Comparison of Text Classifiers},
year = {2016},
isbn = {9781450340694},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/2911451.2911547},
doi = {10.1145/2911451.2911547},
abstract = {How can we know whether one classifier is really better than the other? In the area of text classification, since the publication of Yang and Liu's seminal SIGIR-1999 paper, it has become a standard practice for researchers to apply null-hypothesis significance testing (NHST) on their experimental results in order to establish the superiority of a classifier. However, such a frequentist approach has a number of inherent deficiencies and limitations, e.g., the inability to accept the null hypothesis (that the two classifiers perform equally well), the difficulty to compare commonly-used multivariate performance measures like F1 scores instead of accuracy, and so on. In this paper, we propose a novel Bayesian approach to the performance comparison of text classifiers, and argue its advantages over the traditional frequentist approach based on t-test etc. In contrast to the existing probabilistic model for F1 scores which is unpaired, our proposed model takes the correlation between classifiers into account and thus achieves greater statistical power. Using several typical text classification algorithms and a benchmark dataset, we demonstrate that the our approach provides rich information about the difference between two classifiers' performances.},
booktitle = {Proceedings of the 39th International ACM SIGIR Conference on Research and Development in Information Retrieval},
pages = {15–24},
numpages = {10},
keywords = {bayesian inference, hypothesis testing, performance evaluation, text classification},
location = {Pisa, Italy},
series = {SIGIR '16}
}
@article{Jiang2016,
   abstract = {Naive Bayes (NB) continues to be one of the top 10 data mining algorithms due to its simplicity, efficiency and efficacy. Of numerous proposals to improve the accuracy of naive Bayes by weakening its feature independence assumption, the feature weighting approach has received less attention from researchers. Moreover, to our knowledge, all of the existing feature weighting approaches only incorporate the learned feature weights into the classification of formula of naive Bayes and do not incorporate the learned feature weights into its conditional probability estimates at all. In this paper, we propose a simple, efficient, and effective feature weighting approach, called deep feature weighting (DFW), which estimates the conditional probabilities of naive Bayes by deeply computing feature weighted frequencies from training data. Empirical studies on a collection of 36 benchmark datasets from the UCI repository show that naive Bayes with deep feature weighting rarely degrades the quality of the model compared to standard naive Bayes and, in many cases, improves it dramatically. Besides, we apply the proposed deep feature weighting to some state-of-the-art naive Bayes text classifiers and have achieved remarkable improvements.},
   author = {Liangxiao Jiang and Chaoqun Li and Shasha Wang and Lungan Zhang},
   doi = {10.1016/J.ENGAPPAI.2016.02.002},
   issn = {0952-1976},
   journal = {Engineering Applications of Artificial Intelligence},
   keywords = {Correlation-based feature selection,Feature weighting,Naive Bayes,Text classification},
   month = {6},
   pages = {26-39},
   publisher = {Pergamon},
   title = {Deep feature weighting for naive Bayes and its application to text classification},
   volume = {52},
   url = {https://www.sciencedirect.com/science/article/abs/pii/S0952197616300112?via%3Dihub},
   year = {2016}
}



@InProceedings{10.1007/3-540-45683-X_45,
author="Kim, Sang-Bum
and Rim, Hae-Chang
and Yook, DongSuk
and Lim, Heui-Seok",
editor="Ishizuka, Mitsuru
and Sattar, Abdul",
title="Effective Methods for Improving Naive Bayes Text Classifiers",
booktitle="PRICAI 2002: Trends in Artificial Intelligence",
year="2002",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="414--423",
abstract="Though naive Bayes text classifiers are widely used because of its simplicity, the techniques for improving performances of these classifiers have been rarely studied. In this paper, we propose and evaluate some general and effective techniques for improving performance of the naive Bayes text classifier. We suggest document model based parameter estimation and document length normalization to alleviate the problems in the traditional multinomial approach for text classification. In addition, Mutual-Information-weighted naive Bayes text classifier is proposed to increase the effect of highly informative words. Our techniques are evaluated on the Reuters21578 and 20 Newsgroups collections, and significant improvements are obtained over the existing multinomial naive Bayes approach.",
isbn="978-3-540-45683-4",
doi = {https://doi.org/10.1007/3-540-45683-X_45}
}

@InProceedings{10.1007/978-3-540-30586-6_76,
author="Schneider, Karl-Michael",
editor="Gelbukh, Alexander",
title="Techniques for Improving the Performance of Naive Bayes for Text Classification",
booktitle="Computational Linguistics and Intelligent Text Processing",
year="2005",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="682--693",
abstract="Naive Bayes is often used in text classification applications and experiments because of its simplicity and effectiveness. However, its performance is often degraded because it does not model text well, and by inappropriate feature selection and the lack of reliable confidence scores. We address these problems and show that they can be solved by some simple corrections. We demonstrate that our simple modifications are able to improve the performance of Naive Bayes for text classification significantly.",
isbn="978-3-540-30586-6",
doi = {https://doi.org/10.1007/978-3-540-30586-6_76}
}

@InProceedings{10.1007/978-3-540-71496-5_73,
author="He, Feng
and Ding, Xiaoqing",
editor="Amati, Giambattista
and Carpineto, Claudio
and Romano, Giovanni",
title="Improving Naive Bayes Text Classifier Using Smoothing Methods",
booktitle="Advances in Information Retrieval",
year="2007",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="703--707",
abstract="The performance of naive Bayes text classifier is greatly influenced by parameter estimation, while the large vocabulary and scarce labeled training set bring difficulty in parameter estimation. In this paper, several smoothing methods are introduced to estimate parameters in naive Bayes text classifier. The proposed approaches can achieve better and more stable performance than Laplace smoothing.",
isbn="978-3-540-71496-5",
doi = {https://doi.org/10.1007/978-3-540-71496-5_73}
}

@InProceedings{10.1007/978-3-540-30549-1_43,
author="Kibriya, Ashraf M.
and Frank, Eibe
and Pfahringer, Bernhard
and Holmes, Geoffrey",
editor="Webb, Geoffrey I.
and Yu, Xinghuo",
title="Multinomial Naive Bayes for Text Categorization Revisited",
booktitle="AI 2004: Advances in Artificial Intelligence",
year="2005",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="488--499",
abstract="This paper presents empirical results for several versions of the multinomial naive Bayes classifier on four text categorization problems, and a way of improving it using locally weighted learning. More specifically, it compares standard multinomial naive Bayes to the recently proposed transformed weight-normalized complement naive Bayes classifier (TWCNB) [1], and shows that some of the modifications included in TWCNB may not be necessary to achieve optimum performance on some datasets. However, it does show that TFIDF conversion and document length normalization are important. It also shows that support vector machines can, in fact, sometimes very significantly outperform both methods. Finally, it shows how the performance of multinomial naive Bayes can be improved using locally weighted learning. However, the overall conclusion of our paper is that support vector machines are still the method of choice if the aim is to maximize accuracy.",
isbn="978-3-540-30549-1",
doi = {https://doi.org/10.1007/978-3-540-30549-1_43}
}

@InProceedings{10.1007/11735106_17,
author="Yin, Ling
and Power, Richard",
editor="Lalmas, Mounia
and MacFarlane, Andy
and R{\"u}ger, Stefan
and Tombros, Anastasios
and Tsikrika, Theodora
and Yavlinsky, Alexei",
title="Adapting the Naive Bayes Classifier to Rank Procedural Texts",
booktitle="Advances in Information Retrieval",
year="2006",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="179--190",
abstract="This paper presents a machine-learning approach for ranking web documents according to the proportion of procedural text they contain. By `procedural text' we refer to ordered lists of steps, which are very common in some instructional genres such as online manuals. Our initial training corpus is built up by applying some simple heuristics to select documents from a large collection and contains only a few documents with a large proportion of procedural texts. We adapt the Naive Bayes classifier to better fit this less than ideal training corpus. This adapted model is compared with several other classifiers in ranking procedural texts using different sets of features and is shown to perform well when only highly distinctive features are used.",
isbn="978-3-540-33348-7",
doi = {https://doi.org/10.1007/11735106_17}
}

@article{CHEN20095432,
title = {Feature selection for text classification with Naïve Bayes},
journal = {Expert Systems with Applications},
volume = {36},
number = {3, Part 1},
pages = {5432-5435},
year = {2009},
issn = {0957-4174},
doi = {https://doi.org/10.1016/j.eswa.2008.06.054},
url = {https://www.sciencedirect.com/science/article/pii/S0957417408003564},
author = {Jingnian Chen and Houkuan Huang and Shengfeng Tian and Youli Qu},
keywords = {Text classification, Feature selection, Text preprocessing, Naïve Bayes},
abstract = {As an important preprocessing technology in text classification, feature selection can improve the scalability, efficiency and accuracy of a text classifier. In general, a good feature selection method should consider domain and algorithm characteristics. As the Naïve Bayesian classifier is very simple and efficient and highly sensitive to feature selection, so the research of feature selection specially for it is significant. This paper presents two feature evaluation metrics for the Naïve Bayesian classifier applied on multi-class text datasets: Multi-class Odds Ratio (MOR), and Class Discriminating Measure (CDM). Experiments of text classification with Naïve Bayesian classifiers were carried out on two multi-class texts collections. As the results indicate, CDM and MOR gain obviously better selecting effect than other feature selection approaches.}
}

@article{ZHANG20112160,
title = {An Improvement to Naive Bayes for Text Classification},
journal = {Procedia Engineering},
volume = {15},
pages = {2160-2164},
year = {2011},
note = {CEIS 2011},
issn = {1877-7058},
doi = {https://doi.org/10.1016/j.proeng.2011.08.404},
url = {https://www.sciencedirect.com/science/article/pii/S1877705811019059},
author = {Wei Zhang and Feng Gao},
keywords = {Text classification, Feature selection, Machine learning, Naïve Bayes},
abstract = {Naïve Bayes classifiers which are widely used for text classification in machine learning are based on the conditional probability of features belonging to a class, which the features are selected by feature selection methods. In this paper, an auxiliary feature method is proposed. It determines features by an existing feature selection method, and selects an auxiliary feature which can reclassify the text space aimed at the chosen features. Then the corresponding conditional probability is adjusted in order to improve classification accuracy. Illustrative examples show that the proposed meth-od indeed improves the performance of naïve Bayes classifier.}
}

@article{FENG2015109,
title = {Feature subset selection using naive Bayes for text classification},
journal = {Pattern Recognition Letters},
volume = {65},
pages = {109-115},
year = {2015},
issn = {0167-8655},
doi = {https://doi.org/10.1016/j.patrec.2015.07.028},
url = {https://www.sciencedirect.com/science/article/pii/S0167865515002378},
author = {Guozhong Feng and Jianhua Guo and Bing-Yi Jing and Tieli Sun},
keywords = {Bayesian model averaging, Global selection index, Latent selection augmented naive Bayes, Local selection index, Text classification},
abstract = {Feature subset selection is known to improve text classification performance of various classifiers. The model using the selected features is often regarded as if it had generated the data. By taking its uncertainty into account, the discrimination capabilities can be measured by a global selection index (GSI), which can be used in the prediction function. In this paper, we propose a latent selection augmented naive (LSAN) Bayes classifier. By introducing a latent feature selection indicator, the GSI can be factorized into each local selection index (LSI). Using conjugate priors, the LSI for feature evaluation can be explicitly calculated. Then the feature subset selection models can be pruned by thresholding the LSIs, and the LSAN classifier can be achieved by the product of a small percentage of single feature model averages. The numerical results on some real datasets show that the proposed method outperforms the contrast feature weighting methods, and is very competitive if compared with some other commonly used classifiers such as SVM.}
}

@article{YOUN2009477,
title = {Class dependent feature scaling method using naive Bayes classifier for text datamining},
journal = {Pattern Recognition Letters},
volume = {30},
number = {5},
pages = {477-485},
year = {2009},
issn = {0167-8655},
doi = {https://doi.org/10.1016/j.patrec.2008.11.013},
url = {https://www.sciencedirect.com/science/article/pii/S0167865508003553},
author = {Eunseog Youn and Myong K. Jeong},
keywords = {Classification, Feature selection, Naive Bayes classifier, Recursive feature elimination},
abstract = {The problem of feature selection is to find a subset of features for optimal classification. A critical part of feature selection is to rank features according to their importance for classification. The naive Bayes classifier has been extensively used in text categorization. We have developed a new feature scaling method, called class–dependent–feature–weighting (CDFW) using naive Bayes (NB) classifier. A new feature scaling method, CDFW–NB–RFE, combines CDFW and recursive feature elimination (RFE). Our experimental results showed that CDFW–NB–RFE outperformed other popular feature ranking schemes used on text datasets.}
}

@article{ZHANG2016137,
title = {Two feature weighting approaches for naive Bayes text classifiers},
journal = {Knowledge-Based Systems},
volume = {100},
pages = {137-144},
year = {2016},
issn = {0950-7051},
doi = {https://doi.org/10.1016/j.knosys.2016.02.017},
url = {https://www.sciencedirect.com/science/article/pii/S0950705116001039},
author = {Lungan Zhang and Liangxiao Jiang and Chaoqun Li and Ganggang Kong},
keywords = {Naive Bayes text classifiers, Feature weighting, Gain ratio, Decision tree},
abstract = {This paper works on feature weighting approaches for naive Bayes text classifiers. Almost all existing feature weighting approaches for naive Bayes text classifiers have some defects: limited improvement to classification performance of naive Bayes text classifiers or sacrificing the simplicity and execution time of the final models. In fact, feature weighting is not new for machine learning community, and many researchers have made fruitful efforts in the field of feature weighting. This paper reviews some simple and efficient feature weighting approaches designed for standard naive Bayes classifiers, and adapts them for naive Bayes text classifiers. As a result, this paper proposes two adaptive feature weighting approaches for naive Bayes text classifiers. Experimental results based on benchmark and real-world data show that, compared to their competitors, our feature weighting approaches show higher classification accuracy, yet at the same time maintain the simplicity and lower execution time of the final models.}
}

@INPROCEEDINGS{4554061,
  author={Ding, Wang and Yu, Songnian and Wang, Qianfeng and Yu, Jiaqi and Guo, Qiang},
  booktitle={2008 International Symposiums on Information Processing}, 
  title={A Novel Naive Bayesian Text Classifier}, 
  year={2008},
  volume={},
  number={},
  pages={78-82},
  abstract={The naive Bayesian (NB) classifier is one of the simple but most efficient and stable classification methods. The great efficiency of NB is mainly because of the conditionally independence assumption among the attributes, which is problematic in practice especially while the attributes are strongly correlated. In this paper, we propose a novel NB text classifier, package and combined naive Bayesian text classifier (PC-NB) that relaxes the independence assumption. The main aim of PC-NB is to make naive Bayesian classifier be more accurate without efficiency reduction. A set of experiments were performed and the results of the analysis and experiment indicate that the proposed classifier is more accurate and powerful while the attributes of an instance are strongly correlated.},
  keywords={Bayesian methods;Text categorization;Niobium;Packaging;Artificial intelligence;Text mining;Information processing;Performance analysis;Support vector machines;Support vector machine classification;Text classification;Naive bayesian;Data mining},
  doi={10.1109/ISIP.2008.54},
  ISSN={},
  month={May},}

@article{ELHINDI2020106652,
title = {Lazy fine-tuning algorithms for naïve Bayesian text classification},
journal = {Applied Soft Computing},
volume = {96},
pages = {106652},
year = {2020},
issn = {1568-4946},
doi = {https://doi.org/10.1016/j.asoc.2020.106652},
url = {https://www.sciencedirect.com/science/article/pii/S1568494620305901},
author = {Khalil M. {El Hindi} and Reem R. Aljulaidan and Hussien AlSalman},
keywords = {Fine-tuning Naïve Bayes, Document categorization, Local learning, Multinomial text classification, Complement NB, One-versus-all NB},
abstract = {The naïve Bayes (NB) learning algorithm is widely applied in many fields, particularly in text classification. However, its performance decreases when it is used in domains where its naïve assumption is violated or when the training set is too small to find accurate estimations of the probabilities. In this study, we propose a lazy fine-tuning naïve Bayes (LFTNB) method to address both problems. We propose a local fine-tuning algorithm that uses the nearest neighbors of a query instance to fine-tune the probability terms used by NB. Applying the nearest neighbors only makes the independence assumption more likely to be valid, whereas the fine-tuning algorithm is used to find more accurate estimations of the probability terms. The performance of the LFTNB approach was evaluated using 47 UCI datasets. The results show that the LFTNB method achieves superior performance than classical NB, eager FTNB, and k-nearest neighbor algorithms. We also propose eager and lazy fine-tuning versions of powerful NB-based text classification algorithms, namely, multinomial NB, complement NB, and one-versus-all NB. The empirical results using 18 UCI text classification datasets show that the proposed methods outperform untuned versions of these algorithms.}
}

@article{LU2010598,
title = {Chinese text classification by the Naïve Bayes Classifier and the associative classifier with multiple confidence threshold values},
journal = {Knowledge-Based Systems},
volume = {23},
number = {6},
pages = {598-604},
year = {2010},
issn = {0950-7051},
doi = {https://doi.org/10.1016/j.knosys.2010.04.004},
url = {https://www.sciencedirect.com/science/article/pii/S0950705110000638},
author = {Shing-Hwa Lu and Ding-An Chiang and Huan-Chao Keh and Hui-Hua Huang},
keywords = {Association classification, Text classification, Text mining, Text categorization},
abstract = {Each type of classifier has its own advantages as well as certain shortcomings. In this paper, we take the advantages of the associative classifier and the Naïve Bayes Classifier to make up the shortcomings of each other, thus improving the accuracy of text classification. We will classify the training cases with the Naïve Bayes Classifier and set different confidence threshold values for different class association rules (CARs) to different classes by the obtained classification accuracy rate of the Naïve Bayes Classifier to the classes. Since the accuracy rates of all selected CARs of the class are higher than that obtained by the Naïve Bayes Classifier, we could further optimize the classification result through these selected CARs. Moreover, for those unclassified cases, we will classify them with the Naïve Bayes Classifier. The experimental results show that combining the advantages of these two different classifiers better classification result can be obtained than with a single classifier.}
}

@article{KIM2018128,
title = {Towards perfect text classification with Wikipedia-based semantic Naïve Bayes learning},
journal = {Neurocomputing},
volume = {315},
pages = {128-134},
year = {2018},
issn = {0925-2312},
doi = {https://doi.org/10.1016/j.neucom.2018.07.002},
url = {https://www.sciencedirect.com/science/article/pii/S0925231218308282},
author = {Han-joon Kim and Jiyun Kim and Jinseog Kim and Pureum Lim},
keywords = {Text classification, Naïve Bayes learning, Tensor space, Wikipedia, Semantic features},
abstract = {This paper suggests a novel way of dramatically improving the Naïve Bayes text classifier with our semantic tensor space model for document representation. In our work, we intend to achieve a perfect text classification with the semantic Naïve Bayes learning that incorporates the semantic concept features into term feature statistics; for this, the Naïve Bayes learning is semantically augmented under the tensor space model where the ‘concept’ space is regarded as an independent space equated with the ‘term’ and ‘document’ spaces, and it is produced with concept-level informative Wikipedia pages associated with a given document corpus. Through extensive experiments using three popular document corpora including Reuters-21578, 20Newsgroups, and OHSUMED corpora, we prove that the proposed method not only has superiority over the recent deep learning-based classification methods but also shows nearly perfect classification performance.}
}

@inproceedings{10.5555/1619645.1619732,
author = {Dai, Wenyuan and Xue, Gui-Rong and Yang, Qiang and Yu, Yong},
title = {Transferring naive bayes classifiers for text classification},
year = {2007},
isbn = {9781577353232},
publisher = {AAAI Press},
abstract = {A basic assumption in traditional machine learning is that the training and test data distributions should be identical. This assumption may not hold in many situations in practice, but we may be forced to rely on a different-distribution data to learn a prediction model. For example, this may be the case when it is expensive to label the data in a domain of interest, although in a related but different domain there may be plenty of labeled data available. In this paper, we propose a novel transfer-learning algorithm for text classification based on an EM-based Naive Bayes classifiers. Our solution is to first estimate the initial probabilities under a distribution Dl of one labeled data set, and then use an EM algorithm to revise the model for a different distribution Du of the test data which are unlabeled. We show that our algorithm is very effective in several different pairs of domains, where the distances between the different distributions are measured using the Kullback-Leibler (KL) divergence. Moreover, KL-divergence is used to decide the trade-off parameters in our algorithm. In the experiment, our algorithm outperforms the traditional supervised and semi-supervised learning algorithms when the distributions of the training and test sets are increasingly different.},
booktitle = {Proceedings of the 22nd National Conference on Artificial Intelligence - Volume 1},
pages = {540–545},
numpages = {6},
location = {Vancouver, British Columbia, Canada},
series = {AAAI'07},
url = {https://dl.acm.org/doi/10.5555/1619645.1619732}
}
```

Realizalo la matriz en markdown y presentala en un bloque de codigo markdown para poder copiar su contenido.

# prompt8
Ahora necesito que hagas esto:

Clasificar las fuentes por relevancia para el proyecto (alta, media, baja).

Recuerda que el tema inicial de donde surgió todo esto es: "¿Qué tan efectivo es Naive Bayes en clasificación de texto?".

# prompt9
Ahora hazme la tabla final en html siguiendo esta plantilla html:
```html
<table border="1">
  <thead>
    <tr>
      <th>Trabajo</th>
      <th>Nivel Jerarquía</th>
      <th>Antecedentes</th>
      <th>Estado Arte</th>
      <th>Trabajos Relacionados</th>
    </tr>
  </thead>

  <tbody>
    <!-- Trabajo 1 -->
    <tr>
      <td rowspan="3">1</td>
      <td>Alto</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Medio</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bajo</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>

    <!-- ... -->
    <tr>
      <td rowspan="3">...</td>
      <td>Alto</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Medio</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bajo</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>

    <!-- Trabajo 20 -->
    <tr>
      <td rowspan="3">20</td>
      <td>Alto</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Medio</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bajo</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
```

# prompt10
No incluyas conclusiones y recomendaciones en el latex que generes ya que el docente dijo que por el momento que eso no. Incluyes la seccion de declaracion de la IA.

matriz en markdown (para los resultados de la plantilla latex):
```markdown
| Autor(es) | Año | Título | Tipo de fuente | Resumen del aporte | Método usado | Hallazgos clave |
|---|---:|---|---|---|---|---|
| Sang Bum Kim, Kyoung Soo Han, Hae Chang Rim, Sung Hyon Myaeng | 2006 | Some effective techniques for naive bayes text classification | Artículo de revista (IEEE) | Propone mejoras prácticas para corregir debilidades del Naive Bayes en clasificación de texto. | Normalización por documento y ponderación de características. | Las mejoras incrementan notablemente la precisión y compiten con clasificadores como SVM. |
| Ketkaew Sangounpao, Pornsiri Muenchaisri | 2019 | Ontology-Based Naive Bayes Short Text Classification Method for a Small Dataset | Artículo de conferencia (IEEE) | Presenta una estrategia para clasificar texto corto en un dominio contable con pocos datos. | Bolsa de palabras basada en ontología + Naive Bayes + validación cruzada. | Supera el 80% de clasificación correcta y mejora frente a métodos tradicionales. |
| Eibe Frank, Remco R. Bouckaert | 2006 | Naive Bayes for Text Classification with Unbalanced Classes | Capítulo de libro / conferencia (Springer) | Analiza cómo Naive Bayes se comporta con clases desbalanceadas en clasificación documental. | Transformaciones de datos y ajuste de priors/atributos. | Las correcciones mejoran el AUC y hacen más robusto el MNB en clases desbalanceadas. |
| Dell Zhang, Jun Wang, Emine Yilmaz, Xiaoling Wang, Yuxin Zhou | 2016 | Bayesian Performance Comparison of Text Classifiers | Artículo de conferencia (ACM) | Propone una forma bayesiana de comparar clasificadores de texto con mayor poder estadístico. | Modelo bayesiano para comparación de desempeño. | Aporta una alternativa más informativa que pruebas frecuentistas tradicionales. |
| Liangxiao Jiang, Chaoqun Li, Shasha Wang, Lungan Zhang | 2016 | Deep feature weighting for naive Bayes and its application to text classification | Artículo de revista (ScienceDirect) | Mejora Naive Bayes mediante ponderación profunda de características. | Feature weighting profundo aplicado a frecuencias condicionales. | En múltiples conjuntos de datos mejora o mantiene el rendimiento frente a NB estándar. |
| Sang-Bum Kim, Hae-Chang Rim, DongSuk Yook, Heui-Seok Lim | 2002 | Effective Methods for Improving Naive Bayes Text Classifiers | Capítulo de libro / conferencia (Springer) | Presenta técnicas generales para mejorar NB en texto. | Estimación basada en modelo documental, normalización de longitud y ponderación por mutual information. | Las técnicas producen mejoras significativas sobre el NB multinomial tradicional. |
| Karl-Michael Schneider | 2005 | Techniques for Improving the Performance of Naive Bayes for Text Classification | Capítulo de libro / conferencia (Springer) | Examina por qué NB pierde rendimiento y cómo corregirlo de forma simple. | Correcciones para modelado textual, selección de características y scores de confianza. | Las modificaciones propuestas mejoran significativamente la clasificación. |
| Feng He, Xiaoqing Ding | 2007 | Improving Naive Bayes Text Classifier Using Smoothing Methods | Capítulo de libro / conferencia (Springer) | Explora métodos de suavizado para estabilizar estimaciones en NB. | Diferentes técnicas de smoothing para estimar parámetros. | Los métodos propuestos superan a Laplace smoothing en estabilidad y desempeño. |
| Ashraf M. Kibriya, Eibe Frank, Bernhard Pfahringer, Geoffrey Holmes | 2005 | Multinomial Naive Bayes for Text Categorization Revisited | Capítulo de libro / conferencia (Springer) | Revisa y compara variantes de Naive Bayes multinomial para categorización de texto. | Experimentos comparativos; TF-IDF, normalización y aprendizaje ponderado local. | TF-IDF y normalización ayudan; SVM aún puede superar a NB en varios conjuntos. |
| Ling Yin, Richard Power | 2006 | Adapting the Naive Bayes Classifier to Rank Procedural Texts | Capítulo de libro / conferencia (Springer) | Adapta NB para ranking de textos procedimentales en la web. | Clasificación/ranking con Naive Bayes y selección de rasgos distintivos. | Funciona bien cuando se usan características altamente informativas. |
| Jingnian Chen, Houkuan Huang, Shengfeng Tian, Youli Qu | 2009 | Feature selection for text classification with Naïve Bayes | Artículo de revista (ScienceDirect) | Propone métricas de selección de rasgos específicas para NB. | MOR y CDM para selección de características. | Las métricas propuestas mejoran claramente la selección y la precisión. |
| Wei Zhang, Feng Gao | 2011 | An Improvement to Naive Bayes for Text Classification | Artículo de revista / congreso (ScienceDirect) | Introduce una característica auxiliar para mejorar la clasificación con NB. | Método de feature auxiliar y ajuste de probabilidades condicionales. | La propuesta mejora la exactitud frente al NB convencional. |
| Guozhong Feng, Jianhua Guo, Bing-Yi Jing, Tieli Sun | 2015 | Feature subset selection using naive Bayes for text classification | Artículo de revista (ScienceDirect) | Plantea una selección de subconjuntos de características con base probabilística. | LSAN Bayes con índices locales y globales de selección. | Supera métodos de ponderación comparados y compite bien con SVM. |
| Eunseog Youn, Myong K. Jeong | 2009 | Class dependent feature scaling method using naive Bayes classifier for text datamining | Artículo de revista (ScienceDirect) | Propone una escala de características dependiente de la clase para NB en minería de texto. | Class-dependent feature weighting + recursive feature elimination. | El esquema CDFW-NB-RFE supera esquemas populares de ranking de rasgos. |
| Lungan Zhang, Liangxiao Jiang, Chaoqun Li, Ganggang Kong | 2016 | Two feature weighting approaches for naive Bayes text classifiers | Artículo de revista (ScienceDirect) | Presenta dos enfoques de ponderación para mejorar NB en texto. | Adaptación de técnicas de feature weighting y gain ratio. | Aumenta la precisión manteniendo simplicidad y bajo costo computacional. |
| Wang Ding, Songnian Yu, Qianfeng Wang, Jiaqi Yu, Qiang Guo | 2008 | A Novel Naive Bayesian Text Classifier | Artículo de conferencia (IEEE) | Propone un clasificador NB que relaja la independencia condicional. | Package and combined naive Bayesian text classifier (PC-NB). | Mejora la exactitud cuando las características están fuertemente correlacionadas. |
| Khalil M. El Hindi, Reem R. Aljulaidan, Hussien AlSalman | 2020 | Lazy fine-tuning algorithms for naïve Bayesian text classification | Artículo de revista (ScienceDirect) | Introduce una estrategia de ajuste local para NB en clasificación de texto. | Lazy fine-tuning con vecinos cercanos; variantes para multinomial, complement y one-vs-all NB. | Mejora NB clásico y sus variantes en varios conjuntos de datos. |
| Shing-Hwa Lu, Ding-An Chiang, Huan-Chao Keh, Hui-Hua Huang | 2010 | Chinese text classification by the Naïve Bayes Classifier and the associative classifier with multiple confidence threshold values | Artículo de revista (ScienceDirect) | Combina Naive Bayes con clasificadores asociativos para mejorar el texto en chino. | Híbrido NB + reglas de asociación con umbrales de confianza múltiples. | El enfoque combinado mejora el resultado respecto a usar un solo clasificador. |
| Han-joon Kim, Jiyun Kim, Jinseog Kim, Pureum Lim | 2018 | Towards perfect text classification with Wikipedia-based semantic Naïve Bayes learning | Artículo de revista (ScienceDirect) | Integra semántica basada en Wikipedia para enriquecer NB. | Semantic Naïve Bayes learning con tensor space model. | Reporta rendimiento muy alto y superioridad frente a varios enfoques recientes. |
| Wenyuan Dai, Gui-Rong Xue, Qiang Yang, Yong Yu | 2007 | Transferring naive bayes classifiers for text classification | Artículo de conferencia (ACM) | Propone transfer learning con NB para cuando los datos de entrenamiento y prueba difieren. | NB con EM para adaptar probabilidades entre dominios. | Supera métodos supervisados y semi-supervisados cuando hay cambio de distribución. |
```

Ahora sí, procede con la siguiente plantilla en latex:
```latex
\documentclass[11pt,a4paper]{article}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish]{babel}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{array}
\usepackage{tabularx}
\usepackage{makecell}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{helvet}
\usepackage{ragged2e}
\usepackage{enumitem}
\usepackage{setspace}

\renewcommand{\familydefault}{\sfdefault}
\geometry{
  a4paper,
  left=3.0cm,
  right=3.0cm,
  top=2.35cm,
  bottom=2.35cm,
  headheight=1.9cm,
  headsep=0.45cm
}

\setlength{\parindent}{0pt}
\setlength{\parskip}{0.22em}
\setlength{\tabcolsep}{6pt}
\renewcommand{\arraystretch}{1.08}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\includegraphics[height=1.35cm]{reporte_tecnico_overleaf_logo.png}}
\fancyhead[R]{\vspace{0.1cm}\small FEIRNNR - Carrera de Computación}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\footrulewidth}{0pt}
\makeatletter
\renewcommand{\headrule}{%
  {\color{gray!65}\hrule width\headwidth height\headrulewidth \vskip-\headrulewidth}%
}
\makeatother

\titleformat{\section}
  {\bfseries\fontsize{15}{17}\selectfont}
  {\thesection.}{0.8em}{}
\titlespacing*{\section}{0pt}{0.7ex}{0.2ex}

\newcolumntype{L}[1]{>{\RaggedRight\arraybackslash}p{#1}}
\newcolumntype{Y}{>{\RaggedRight\arraybackslash}X}

\begin{document}
\thispagestyle{fancy}

\vspace*{0.15cm}

\begin{center}
{\bfseries\fontsize{23}{26}\selectfont
Reporte Técnico de Actividades\\
Práctico-Experimentales Nro. 001\par}
\end{center}

\section{Datos de Identificación del Estudiante y la Práctica}

\noindent
\begin{tabularx}{\textwidth}{|L{0.43\textwidth}|Y|}
\hline
\textbf{Nombre del estudiante(s)} & Edison Leonardo Coronel Romero \\ \hline
\textbf{Asignatura} & Desarrollo Basado en Plataformas \\ \hline
\textbf{Ciclo} & 5 A \\ \hline
\textbf{Unidad} & 1 \\ \hline
\textbf{Resultado de aprendizaje de la unidad} &  \\ \hline
\textbf{Práctica Nro.} & 001 \\ \hline
\textbf{Título de la Práctica} & Implementar un servicio REST con Node.js \\ \hline
\textbf{Nombre del Docente} & Edison Leonardo Coronel Romero \\ \hline
\textbf{Fecha} & Viernes 3 de octubre \\ \hline
\textbf{Horario} & 07h30 -- 10h30 \\ \hline
\textbf{Lugar} & \makecell[tl]{Laboratorio Computación aplicada\\Laboratorio Desarrollo de Software\\Laboratorio de redes y Sistemas Operativos\\Laboratorio Virtual\\EVA\\Aula} \\ \hline
\textbf{Tiempo planificado en el Sílabo} & 3 horas \\ \hline
\end{tabularx}

\section{Objetivo(s) de la Práctica}
Escriba el objetivo de la práctica (copiado de la guía proporcionada por el docente).

\section{Materiales, Reactivos, Equipos y Herramientas}
Liste los materiales, reactivos, equipos y herramientas utilizados en la práctica, confirmando los de la guía o agregando los adicionales.

\section{Procedimiento / Metodología Ejecutada}
Describa brevemente los pasos que siguió durante la ejecución de la práctica.

\section{Resultados}
Incluya evidencias del trabajo realizado (tablas, gráficos, capturas de pantalla, registros de ejecución, modelos, programas, informes, etc.).

\newpage

\section{Preguntas de Control}
Responda a las preguntas del docente.

\section{Conclusiones}
Redacte las principales conclusiones de la práctica, vinculándolas con el objetivo planteado.

\section{Recomendaciones}
Incluya sugerencias para mejorar la práctica o su aplicación en casos reales.

\section{Bibliografía / Referencias}
Liste las fuentes adicionales consultadas siguiendo el formato IEEE.

\section{Anexos}
Recursos de apoyo para cada una de las secciones anteriores.

\end{document}
```



