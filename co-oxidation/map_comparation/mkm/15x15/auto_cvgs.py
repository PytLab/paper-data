pCO = [1e-05, 0.03572357142857143, 0.07143714285714285, 0.10715071428571428, 0.14286428571428572, 0.17857785714285715, 0.21429142857142858, 0.250005, 0.28571857142857143, 0.3214321428571429, 0.3571457142857143, 0.3928592857142857, 0.42857285714285714, 0.4642864285714286, 0.5]

pO2 = [1e-05, 0.03572357142857143, 0.07143714285714285, 0.10715071428571428, 0.14286428571428572, 0.17857785714285715, 0.21429142857142858, 0.250005, 0.28571857142857143, 0.3214321428571429, 0.3571457142857143, 0.3928592857142857, 0.42857285714285714, 0.4642864285714286, 0.5]

adsorbates = ('CO_s', 'O_s')

cvgs_O = [[5.723811274412445e-23, 4.485135482507735e-30, 1.1215978144297757e-30, 4.985344407005573e-31, 2.8043870849378143e-31, 1.7948579891781411e-31, 1.246452424356264e-31, 9.157731748235191e-32, 7.01145849235699e-32, 5.539960893202134e-32, 4.48739625758848e-32, 3.708610787680601e-32, 3.116276453168126e-32, 2.655298335103783e-32, 2.289524449079017e-32], [0.999240559081131, 1.602250577695352e-26, 4.006747963615886e-27, 1.7809430701182755e-27, 1.0018272233770031e-27, 6.411873757770211e-28, 4.452773221182943e-28, 3.2714688421723966e-28, 2.504743382590455e-28, 1.979071886709997e-28, 1.6030582072913815e-28, 1.3248482236858684e-28, 1.1132452446097571e-28, 9.48567397340278e-29, 8.178999019049687e-29], [0.9996202263813563, 3.204052641852034e-26, 8.012374329423333e-27, 3.561387605797034e-27, 2.0033740080458868e-27, 1.2821952657552776e-27, 8.90429998994227e-28, 6.542021911170369e-28, 5.008785619331908e-28, 3.9575897773308195e-28, 3.2056676749571e-28, 2.6493255862930337e-28, 2.2261788615742435e-28, 1.8968692648470801e-28, 1.6355708513650542e-28], [0.9997468057700615, 4.8058547060182973e-26, 1.2018000695236772e-26, 5.341832141476976e-27, 3.0049207927151454e-27, 1.923203155733688e-27, 1.3355826758702337e-27, 9.81257498016874e-28, 7.512827856073595e-28, 5.936107667951788e-28, 4.808277142622914e-28, 3.9738029489002656e-28, 3.339112478538776e-28, 2.8451711323539143e-28, 2.4532418008251664e-28], [0.9998100998944623, 0.31594145209213087, 1.6023627061056202e-26, 7.122276677158102e-27, 4.006467577384779e-27, 2.5642110457122515e-27, 1.7807353527463143e-27, 1.3083128049167514e-27, 1.0016870092815517e-27, 7.914625558572914e-28, 6.410886610288825e-28, 5.298280311507563e-28, 4.452046095503355e-28, 3.793472999860785e-28, 3.2709127502853005e-28], [0.9998480777868373, 0.4541252937512103, 2.0029253426881623e-26, 8.902721212840412e-27, 5.0080143620547864e-27, 3.205218935690969e-27, 2.2258880296224693e-27, 1.6353681118166683e-27, 1.2520912329557673e-27, 9.893143449194171e-28, 8.013496077954831e-28, 6.622757674114925e-28, 5.564979712467981e-28, 4.741774867367686e-28, 4.088583699745462e-28], [0.9998733969725042, 0.545540698838661, 2.4034879792713037e-26, 1.0683165748523906e-26, 6.0095611467251685e-27, 3.846226825669839e-27, 2.6710407064986986e-27, 1.9624234187166256e-27, 1.5024954566300062e-27, 1.1871661339815584e-27, 9.616105545620933e-28, 7.947235036722353e-28, 6.677913329432653e-28, 5.69007673487462e-28, 4.906254649205674e-28], [0.9998914823944792, 0.6106608944785423, 0.2048004979195724, 1.2463610284208581e-26, 7.011107931395924e-27, 4.487234715648863e-27, 3.116193383375001e-27, 2.289478725616622e-27, 1.7528996803042685e-27, 1.385017923043714e-27, 1.1218715013287129e-27, 9.271712399329845e-28, 7.790846946397369e-28, 6.63837860238159e-28, 5.723925598665856e-28], [0.9999050466192052, 0.6594350333621186, 0.31013517193867773, 1.4244054819894444e-26, 8.012654716067056e-27, 5.1282426056280405e-27, 3.561346060251378e-27, 2.6165340325166595e-27, 2.0033039039785544e-27, 1.5828697121058846e-27, 1.2821324480953426e-27, 1.059618976193738e-27, 8.903780563362134e-28, 7.586680469888592e-28, 6.541596548126093e-28], [0.9999155966655461, 0.6973400160017179, 0.38886218247452725, 1.602449935558149e-26, 9.014201500738563e-27, 5.769250495607372e-27, 4.00649873712783e-27, 2.9435893394167367e-27, 2.253708127652864e-27, 1.780721501168068e-27, 1.4423933948619815e-27, 1.192066712454503e-27, 1.0016714180326945e-27, 8.534982337395627e-28, 7.359267497586358e-28], [0.9999240367616984, 0.7276479539479946, 0.4509890458118965, 0.1400234253407216, 1.0015748285410444e-26, 6.410258385586856e-27, 4.451651414004353e-27, 3.270644646316853e-27, 2.5041123513271962e-27, 1.978573290230268e-27, 1.60265434162863e-27, 1.324514448715272e-27, 1.1129647797291802e-27, 9.483284204902697e-28, 8.176938447046643e-28], [0.9999309423339752, 0.7524360843633212, 0.5014792368110716, 0.23512493059019557, 1.1017295070082698e-26, 7.051266275566492e-27, 4.896804090880953e-27, 3.59769995321701e-27, 2.754516575001552e-27, 2.1764250792924813e-27, 1.762915288395288e-27, 1.4569621849760475e-27, 1.2242581414256702e-27, 1.04315860724098e-27, 8.994609396506952e-28], [0.999936697004394, 0.7730871219710713, 0.5433888029079956, 0.3040404018813517, 1.2018841854755329e-26, 7.692274165546284e-27, 5.341956767757625e-27, 3.924755260117207e-27, 3.004920798675932e-27, 2.37427686835471e-27, 1.923176235161956e-27, 1.5894099212368296e-27, 1.3355515031221653e-27, 1.1379887939916942e-27, 9.812280345967326e-28], [0.999941566359971, 0.7905573341160063, 0.578759816721884, 0.36011349855368213, 1.3020388639428333e-26, 8.333282055526229e-27, 5.7871094446343745e-27, 4.251810567017443e-27, 3.255325022350335e-27, 2.572128657416953e-27, 2.0834371819286334e-27, 1.7218576574976184e-27, 1.446844864818665e-27, 1.2328189807424109e-27, 1.0629951295427706e-27], [0.9999457401072351, 0.8055292551627317, 0.6090234802151979, 0.4072997071335214, 0.17913864081053738, 8.974289945506327e-27, 6.2322621215111914e-27, 4.57886587391772e-27, 3.505729246024761e-27, 2.769980446479211e-27, 2.24369812869532e-27, 1.8543053937584135e-27, 1.558138226515169e-27, 1.3276491674931312e-27, 1.144762224488803e-27]]

cvgs_CO = [[0.9999999855035144, 0.999999999995942, 0.9999999999979707, 0.9999999999986471, 0.9999999999989853, 0.9999999999991882, 0.9999999999993234, 0.9999999999994201, 0.9999999999994926, 0.9999999999995489, 0.999999999999594, 0.999999999999631, 0.9999999999996617, 0.9999999999996877, 0.99999999999971], [5.616063441940599e-10, 0.999999999995942, 0.9999999999979707, 0.9999999999986471, 0.9999999999989853, 0.9999999999991882, 0.9999999999993234, 0.9999999999994201, 0.9999999999994926, 0.9999999999995489, 0.999999999999594, 0.999999999999631, 0.9999999999996617, 0.9999999999996877, 0.99999999999971], [2.807358161791526e-10, 0.999999999995942, 0.9999999999979707, 0.9999999999986471, 0.9999999999989853, 0.9999999999991882, 0.9999999999993234, 0.9999999999994201, 0.9999999999994926, 0.9999999999995489, 0.999999999999594, 0.999999999999631, 0.9999999999996617, 0.9999999999996877, 0.99999999999971], [1.8714224917810952e-10, 0.999999999995942, 0.9999999999979707, 0.9999999999986471, 0.9999999999989853, 0.9999999999991882, 0.9999999999993234, 0.9999999999994201, 0.9999999999994926, 0.9999999999995489, 0.999999999999594, 0.999999999999631, 0.9999999999996617, 0.9999999999996877, 0.99999999999971], [1.4035107784595266e-10, 0.005668085346329064, 0.9999999999979707, 0.9999999999986471, 0.9999999999989853, 0.9999999999991882, 0.9999999999993234, 0.9999999999994201, 0.9999999999994926, 0.9999999999995489, 0.999999999999594, 0.999999999999631, 0.9999999999996617, 0.9999999999996877, 0.99999999999971], [1.1227817068209093e-10, 0.003154738499888164, 0.9999999999979707, 0.9999999999986471, 0.9999999999989853, 0.9999999999991882, 0.9999999999993234, 0.9999999999994201, 0.9999999999994926, 0.9999999999995489, 0.999999999999594, 0.999999999999631, 0.9999999999996617, 0.9999999999996877, 0.99999999999971], [9.356364736113106e-11, 0.0021884403278420585, 0.9999999999979707, 0.9999999999986471, 0.9999999999989853, 0.9999999999991882, 0.9999999999993234, 0.9999999999994201, 0.9999999999994926, 0.9999999999995489, 0.999999999999594, 0.999999999999631, 0.9999999999996617, 0.9999999999996877, 0.99999999999971], [8.019649711138356e-11, 0.0016757833109413412, 0.01998137517508899, 0.9999999999986471, 0.9999999999989853, 0.9999999999991882, 0.9999999999993234, 0.9999999999994201, 0.9999999999994926, 0.9999999999995489, 0.999999999999594, 0.999999999999631, 0.9999999999996617, 0.9999999999996877, 0.99999999999971], [7.017133479628336e-11, 0.0013578637020842492, 0.011545575490706587, 0.9999999999986471, 0.9999999999989853, 0.9999999999991882, 0.9999999999993234, 0.9999999999994201, 0.9999999999994926, 0.9999999999995489, 0.999999999999594, 0.999999999999631, 0.9999999999996617, 0.9999999999996877, 0.99999999999971], [6.237410506490665e-11, 0.0011413866117270174, 0.008185026014792627, 0.9999999999986471, 0.9999999999989853, 0.9999999999991882, 0.9999999999993234, 0.9999999999994201, 0.9999999999994926, 0.9999999999995489, 0.999999999999594, 0.999999999999631, 0.9999999999996617, 0.9999999999996877, 0.99999999999971], [5.6136396081899295e-11, 0.0009844641587866147, 0.006351753574178997, 0.04602575532468762, 0.9999999999989853, 0.9999999999991882, 0.9999999999993234, 0.9999999999994201, 0.9999999999994926, 0.9999999999995489, 0.999999999999594, 0.999999999999631, 0.9999999999996617, 0.9999999999996877, 0.99999999999971], [5.1032865460014464e-11, 0.000865485960955012, 0.005192961442818841, 0.024917895593324583, 0.9999999999989853, 0.9999999999991882, 0.9999999999993234, 0.9999999999994201, 0.9999999999994926, 0.9999999999995489, 0.999999999999594, 0.999999999999631, 0.9999999999996617, 0.9999999999996877, 0.99999999999971], [4.677995727505321e-11, 0.0007721711363895315, 0.004393086246097309, 0.017664083319381723, 0.9999999999989853, 0.9999999999991882, 0.9999999999993234, 0.9999999999994201, 0.9999999999994926, 0.9999999999995489, 0.999999999999594, 0.999999999999631, 0.9999999999996617, 0.9999999999996877, 0.99999999999971], [4.3181366798713056e-11, 0.000697023312770851, 0.003807331722862578, 0.013766440907038996, 0.9999999999989853, 0.9999999999991882, 0.9999999999993234, 0.9999999999994201, 0.9999999999994926, 0.9999999999995489, 0.999999999999594, 0.999999999999631, 0.9999999999996617, 0.9999999999996877, 0.99999999999971], [4.009687828956134e-11, 0.000635207098786029, 0.003359704150849808, 0.011302199337059603, 0.045681987764599294, 0.9999999999991882, 0.9999999999993234, 0.9999999999994201, 0.9999999999994926, 0.9999999999995489, 0.999999999999594, 0.999999999999631, 0.9999999999996617, 0.9999999999996877, 0.99999999999971]]
