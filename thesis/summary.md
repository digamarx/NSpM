Summary
=======

The two goals of the Master thesis were:

- to generate a corpus for the purpose of training the NSpM (and other ML based QA approaches),
- the proof of concept that the NSpM can be used for open domain QA when trained with this corpus.


Corpus generation
-----------------

The first goal was achieved with the generation of a corpus that contains 894,499 pairs of a English question and the equivalent SPARQL. Currently it is the largest QA dataset of this kind (see Table 1). Template pairs were extracted from the LC-QuAD and the QALD-7-Train dataset (Table 2). The generator component of the NSpM, that is responsible for instantiating those templates,  was enhanced through the typing of placeholders which enables a controllable instantiation.
Important criteria for such a corpus are size and naturalness of the questions. Both are issues as described in chapter 4.3.
Apart of templates can not be instantiated e.g. 300 times due to the limited number of matching DBPedia instances, 833 of the 5166 templates could not be instantiated at all. Second, at the moment not all of the instantiations are appropriate and grammatically correct.

<table>
	<thead>
		<tr><th>Dataset       </th><th>Size</th><th>Format of Answer</th> </tr>
	</thead>
	<tbody>
<tr><td>SimpleQuestions </td><td align="right"> 108,442 </td><td> Freebase triple </td></tr>
<tr><td>Free917     </td><td align="right">   917     </td><td>   &lambda;-Calculus  </td></tr>
<tr><td>WebQuestions </td><td align="right"> 5,810 </td><td> Text </td></tr>
<tr><td>QALD-7-Train      </td><td align="right">   215     </td><td>   SPARQL </td></tr>
<tr><td>LC-QuAD     </td><td align="right">   5,000 </td><td>    SPARQL   </td></tr>
<tr><td>WMT En-Fr </td><td align="right"> 36,000,000 </td><td>-</td></tr>
<tr><td>NSpM dataset </td><td align="right"> 894,499 </td><td>SPARQL</td></tr>
	</tbody>
	<caption>Table 1: Comparison of QA datasets and a NMT dataset</caption>
</table>

<table>
	<thead>
		<tr><th>Topic</th><th colspan="2">QALD-7-Train</th><th colspan="2">LC-QuAD</th><th colspan="2">Total</th></tr>
		<tr><td></td><td>#</td><td>%</td><td>#</td><td>%</td><td>#</td><td>%</td></tr>
	</thead>
	<tbody>
		<tr><td>Art   </td><td>   49  </td><td>   24,5 % </td><td>       1199    </td><td>       24,1 % </td><td>       1248        </td><td>   24,2 % </td></tr>
		<tr><td>Geography  </td><td>   47  </td><td>   23,5 % </td><td>       766 </td><td>       15,4 % </td><td>       813     </td><td>   15,7 % </td></tr>
		<tr><td>Sport   </td><td>   12  </td><td>   6,0 %  </td><td>       627 </td><td>       12,6 % </td><td>       639     </td><td>   12,4 % </td></tr>
		<tr><td>Society    </td><td>   15  </td><td>   7,5 %  </td><td>       506 </td><td>       10,2 % </td><td>       521     </td><td>   10,1 % </td></tr>
		<tr><td>Economy  </td><td>   13  </td><td>   6,5 %  </td><td>       463 </td><td>       9,3 %  </td><td>       476     </td><td>   9,2 %  </td></tr>
		<tr><td>Personal  </td><td>   37  </td><td>   18,5 % </td><td>       207 </td><td>       4,2 %  </td><td>       244     </td><td>   4,7 %  </td></tr>
		<tr><td>Science    </td><td>   9   </td><td>   4,5 %  </td><td>       150 </td><td>       3,0 %  </td><td>       159     </td><td>   3,1 %  </td></tr>
		<tr><td>IT  </td><td>   7   </td><td>   3,5 %  </td><td>       104 </td><td>       2,1 %  </td><td>       111     </td><td>   2,1 %  </td></tr>
		<tr><td>Time   </td><td>   6   </td><td>   3,0 %  </td><td>       0   </td><td>       0,0 %  </td><td>       6       </td><td>   0,1 %  </td></tr>
		<tr><td>Other  </td><td>   5   </td><td>   2,5 %  </td><td>       944 </td><td>       19,0 % </td><td>       948     </td><td>   18,4 % </td></tr>
	</tbody>
	<tfoot>
		<tr><td>Duplicates </td><td> 15 </td><td> 8,3% </td><td> 34 </td><td> 0,7 % </td><td> 52 </td><td> 1 % </td></tr>
		<tr><td>Total</td><td>200</td><td></td><td>4966</td><td></td><td>5166</td><td></td></tr>
	</tfoot>
	<caption>Table 2: Templates' topics</caption>
</table>


NSpM Evaluation
---------------

The second goal could not be achieved within the scope of this thesis. The MT reached an average BLEU score of 0.62. The in-depth evaluation and error analysis in chapter 5.2 showed that the main problem is the translation of the entities, from the English labels into the correct IRIs. Better results are obtained at the translation of the query types and the predicates and the syntactic validity of the SPARQL. In chapter 5.3 examples are given that provide evidence that the NSpM can operate in a sensitive and robust manner and handle ambiguity.

<table>
	<thead>
		<tr><th>Model</th><th class="soru">Soru et al.</th><th>1</th><th>2</th><th>3</th><th>4</th></tr>
	</thead>
	<tbody>
		<tr><td>Number of templates</td><td class="soru">38</td><td>   200 </td><td>   407 </td><td>   2,233   </td><td>   5,166</td></tr>
		<!-- <tr><td>davon nicht instanziierte Templates </td><td>   7   </td><td>   10  </td><td>   362 </td><td>   833</td></tr> -->
		<tr><td>Number of generated questions</td><td class="soru">8,544</td><td>   51,292  </td><td>   99,274  </td><td>   390,444 </td><td>   894,499</td></tr>
		<tr><td>Size of English Vocabulary</td><td class="soru">2,063</td><td >   28,869  </td><td>   40,599  </td><td>   84,963  </td><td>   134,788</td></tr>
		<tr><td>Size of SPARQL Vocabulary</td><td class="soru">1,769</td><td>   33,730  </td><td>   51,399  </td><td>   144,720 </td><td>   249,395</td></tr>
		<tr><td>Training time (hh:mm)</td><td class="soru">00:18</td><td>   3:03    </td><td>   4:11    </td><td>   10:33   </td><td>   21:29</td></tr>
		<tr><td>Best BLEU wit test data</td><td class="soru">0.753</td><td>   0.634   </td><td>   0.620   </td><td>   0.619   </td><td>   0.601</td></tr>
	</tbody>
	<caption>Table 3: Training details</caption>
</table>

Table 3 shows training specifics compared with the Soru et al. provided data for their domain specific QA experiment. Four models were trained with four sets of templates. The size of the template sets was gradually increased. Model 1 contains only templates extracted from the QALD-7-Train data set. Model 2 and Model 3 contain also the QALD-7-Train templates but also subsets of templates that are extracted from LC-QuAD. Model 4 contains all extracted templates from QALD-7-Train and LC-QuAD. The training time is given for 12k iterations. It suffers from the increasing size of the vocabulary. Model 4 has a vocabulary that is 7 times bigger than Model 1 and its training time is nearly 7 times longer than for Model 1. The BLEU score for the 4 models is very close to one another. It is clearly worse than the model trained by Soru et al.

Table 4 and Table 5 present the translation quality more detailed. Table 4 shows results that are obtained with corpus test data and Table 5 is based on results for QALD-7-Test and QALD-8-Test data. Query type detection and the generation of valid SPARQL is working in both cases. The translation into SPARQL that contains the correct predicate is working well for the corpus test questions but not for the QALD-7/8 test questions. These question sets contain questions that the NSpM has never seen in training which explains why the results in Table 5 are generally worse than in Table 4. Words that are not contained in the Model's vocabulary have a significant negative impact on the translation process. Furthermore words, that occur rarely in the training data like the most of the entities, are getting a word embedding which is low representative. Therefore translating into the correct entity's IRI are the models' biggest weakness.

<table>
	<thead>
<tr><th>Model</th><th class="soru">Soru et al.</th><th>1</th><th>2</th><th>3</th><th>4</th></tr>
	</thead>
	<tbody>
<tr><td>all predicates detected</td><td class="soru">97.0 %</td><td>   96.5 % </td><td>   96.9 % </td><td>   97.2 % </td><td>      83.0 % </td></tr>
<tr><td>partly detected predicates</td><td class="soru">2.0 %</td><td>   1.2 %  </td><td>   1.1 %  </td><td>   0.9 %  </td><td>      6.7 %  </td></tr>
<tr><td>all entities detected</td><td class="soru">74.5 %</td><td>   1.8 %  </td><td>   0.3 %  </td><td>   0.2 %  </td><td>      0.1 %  </td></tr>
<tr><td>partly detected entities</td><td class="soru">6.5 %</td><td>   29.4 % </td><td>   21.6 % </td><td>   32.3 % </td><td>      25.1 % </td></tr>
<tr><td>correct query type</td><td class="soru">100.0 %</td><td>   100.0 %    </td><td>   100.0 %    </td><td>   100.0 %    </td><td>      99.9 % </td></tr>
<tr><td>valid SPARQL</td><td class="soru">69 %</td><td>   85.6 % </td><td>   90.8 % </td><td>   84.3 % </td><td>      84.0 % </td></tr>
<tr><td>all criteria fulfilled (&asymp; F1-Score)</td><td class="soru">0.55</td><td>0</td>		<td>0.001</td>		<td>0.001</td>		<td>0.001</td></tr>
	</tbody>
	<caption>Table 4: Evaluation based on corpus test data</caption>
</table>

<table>
	<thead>
<tr><th>Model</th><th>1</th><th>2</th><th>3</th><th>4</th></tr>
	</thead>
	<tbody>
<tr><td>all predicates detected </td><td>7.1 % </td><td>	11.9 %</td><td>11.9 %</td><td>17.9 %</td></tr>
<tr><td>partly detected predicates </td><td>8.3 % </td><td>	6.0 %</td><td>4.8 %</td><td>1.2 %</td></tr>
<tr><td>all entities detected </td><td>0.0 % </td><td>	0.0 %</td><td>0.0 %</td><td>1.2 %</td></tr>
<tr><td>partly detected entities</td><td>0.0 % </td><td>	0.0 %</td><td>0.0 %</td><td>0.0 %</td></tr>
<tr><td>correct query type</td><td>72.6 % </td><td>	96.4 %</td><td>98.8 %</td><td>97.6 %</td></tr>
<tr><td>valid SPARQL</td><td>75.0 % </td><td>	79.8 %</td><td>77.4 %</td><td>64.3 %</td></tr>
	</tbody>
	<caption>Table 5: Evaluation based on QALD-7-Test and QALD-8-Test</caption>
</table>



Prospective work
------------

Further research could analyse if

- quality and quantity improvements of the dataset or
- the usage of pre-trained word vectors or
- modifications of the sequence to sequence model (attention/copy mechanism, word and character based encoding like Lukovnikov et al. [2017])

solve the OOV and rare word problem and lead to better results for open domain QA with the NSpM approach.