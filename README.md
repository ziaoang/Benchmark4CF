# Benchmark4CF

## RMSE
|#|ml-100k|ml-1m|ml-10m|ml-20m|netflix|
|:----|:----:|:----:|:----:|:----:|:----:|
|global mean|1.1286|1.1181|1.0599|1.0518|1.0852|
|user mean|1.0469|1.0367|0.9775|0.9640|0.9986|
|item mean|1.0263|0.9809|0.9432|0.9413|1.0112|
|user item mean|0.9861|0.9585|0.9125|0.9053|0.9639|
|libmf|0.9158|0.8771|0.8285|0.8222|0.8792|
|libfm sgd|0.9834|0.8668|0.8020|0.7983|0.8481|
|libfm als|0.9119|0.8484|0.7934|0.7861|0.8406|
|libfm mcmc|0.9096|0.8486|0.7866|0.7788|0.8355|
|svdfeature|0.9023|0.8393|0.7740|0.7638|0.8182|

## MAE
|#|ml-100k|ml-1m|ml-10m|ml-20m|netflix|
|:----|:----:|:----:|:----:|:----:|:----:|
|global mean|0.9475|0.9350|0.8550|0.8407|0.9095|
|user mean|0.8362|0.8300|0.7681|0.7516|0.7980|
|item mean|0.8175|0.7840|0.7376|0.7317|0.8110|
|user item mean|0.7960|0.7726|0.7188|0.7077|0.7810|
|libmf|0.7238|0.6991|0.6467|0.6383|0.6954|
|libfm sgd|0.7497|0.6721|0.6121|0.6053|0.6514|
|libfm als|0.7099|0.6635|0.6068|0.5972|0.6480|
|libfm mcmc|0.7166|0.6684|0.6040|0.5941|0.6483|
|svdfeature|0.7051|0.6583|0.5929|0.5811|0.6337|



#state-of-the-art

## MovieLens 1M
|METHOD|TEST RMSE|
|:----|:----:|
|PMF (Dziugaite & Roy, 2015)|0.883|
|U-RBM (Sedhain et al., 2015)|0.881|
|U-AUTOREC (SEDHAIN ET AL., 2015)|0.874|
|LLORMA-GLOBAL (LEE ET AL., 2013)|0.865|
|I-RBM (Sedhain et al., 2015)|0.854|
|BIASMF (Sedhain et al., 2015)|0.845|
|NNMF (DZIUGAITE & ROY, 2015)|0.843|
|LLORMA-LOCAL (LEE ET AL., 2013)|0.833|
|I-AUTOREC (SEDHAIN ET AL., 2015)|0.831|
|U-CF-NADE-S (SINGLE LAYER)|0.850|
|U-CF-NADE-S (2 LAYERS )|0.845|
|I-CF-NADE-S (SINGLE LAYER)|0.830|
|I-CF-NADE-S (2 LAYERS)|0.829|

## MovieLens 10M
|METHOD|TEST RMSE|
|:----|:----:|
|U-AUTOREC (SEDHAIN ET AL., 2015)|0.867|
|I-RBM (Sedhain et al., 2015)|0.825|
|U-RBM (Sedhain et al., 2015)|0.823|
|LLORMA-GLOBAL (LEE ET AL., 2013)|0.822|
|BIASMF (Sedhain et al., 2015)|0.803|
|LLORMA-LOCAL (LEE ET AL., 2013)|0.782|
|I-AUTOREC (SEDHAIN ET AL., 2015)|0.782|
|U-CF-NADE-S (SINGLE LAYER)|0.772|
|U-CF-NADE-S (2 LAYERS)|0.771|

## Netflix
|METHOD|TEST RMSE|
|:----|:----:|
|LLORMA-GLOBAL (LEE ET AL., 2013)|0.874|
|U-RBM (Sedhain et al., 2015)|0.845|
|BIASMF (Sedhain et al., 2015)|0.844|
|LLORMA-LOCAL (LEE ET AL., 2013)|0.834|
|I-AUTOREC (SEDHAIN ET AL., 2015)|0.823|
|U-CF-NADE-S (SINGLE LAYER)|0.804|
|U-CF-NADE-S (2 LAYERS)|0.803|



