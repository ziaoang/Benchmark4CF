# Benchmark4CF

## RMSE
|METHOD|jester|ml-100k|ml-1m|ml-10m|ml-20m|netflix|
|:----|:----:|:----:|:----:|:----:|:----:|:----:|
|global mean|5.2963&plusmn;0.0051|1.1286&plusmn;0.0073|1.1181&plusmn;0.0008|1.0599&plusmn;0.0006|1.0518&plusmn;0.0003|1.0852&plusmn;0.0002|
|user mean|4.6661&plusmn;0.0034|1.0469&plusmn;0.0053|1.0367&plusmn;0.0019|0.9775&plusmn;0.0005|0.9640&plusmn;0.0006|0.9986&plusmn;0.0001|
|item mean|5.0496&plusmn;0.0046|1.0263&plusmn;0.0062|0.9809&plusmn;0.0019|0.9432&plusmn;0.0008|0.9413&plusmn;0.0003|1.0112&plusmn;0.0002|
|user item mean|4.6056&plusmn;0.0038|0.9861&plusmn;0.0055|0.9585&plusmn;0.0019|0.9125&plusmn;0.0007|0.9053&plusmn;0.0003|0.9639&plusmn;0.0002|
|libmf|4.2274&plusmn;0.0047|0.9158&plusmn;0.0034|0.8771&plusmn;0.0026|0.8285&plusmn;0.0007|0.8222&plusmn;0.0005|0.8792&plusmn;0.0006|
|libfm sgd|4.4610&plusmn;0.0249|0.9834&plusmn;0.0073|0.8668&plusmn;0.0027|0.8020&plusmn;0.0016|0.7983&plusmn;0.0068|0.8481&plusmn;0.0018|
|libfm als|4.3331&plusmn;0.0086|0.9119&plusmn;0.0047|0.8484&plusmn;0.0028|0.7934&plusmn;0.0006|0.7861&plusmn;0.0005|0.8406&plusmn;0.0001|
|libfm mcmc|4.2439&plusmn;0.0450|0.9096&plusmn;0.0046|0.8486&plusmn;0.0030|0.7866&plusmn;0.0004|0.7788&plusmn;0.0004|0.8355&plusmn;0.0005|
|svdfeature|4.0651&plusmn;0.0045|0.9023&plusmn;0.0039|0.8393&plusmn;0.0030|0.7740&plusmn;0.0005|0.7638&plusmn;0.0004|0.8182&plusmn;0.0002|

## MAE
|METHOD|jester|ml-100k|ml-1m|ml-10m|ml-20m|netflix|
|:----|:----:|:----:|:----:|:----:|:----:|:----:|
|global mean|4.4370&plusmn;0.0049|0.9475&plusmn;0.0046|0.9350&plusmn;0.0011|0.8550&plusmn;0.0005|0.8407&plusmn;0.0004|0.9095&plusmn;0.0002|
|user mean|3.7478&plusmn;0.0023|0.8362&plusmn;0.0040|0.8300&plusmn;0.0017|0.7681&plusmn;0.0005|0.7516&plusmn;0.0005|0.7980&plusmn;0.0001|
|item mean|4.1799&plusmn;0.0042|0.8175&plusmn;0.0056|0.7840&plusmn;0.0012|0.7376&plusmn;0.0006|0.7317&plusmn;0.0002|0.8110&plusmn;0.0002|
|user item mean|3.8144&plusmn;0.0039|0.7960&plusmn;0.0044|0.7726&plusmn;0.0014|0.7188&plusmn;0.0005|0.7077&plusmn;0.0003|0.7810&plusmn;0.0001|
|libmf|3.2238&plusmn;0.0037|0.7238&plusmn;0.0029|0.6991&plusmn;0.0015|0.6467&plusmn;0.0006|0.6383&plusmn;0.0004|0.6954&plusmn;0.0004|
|libfm sgd|3.3827&plusmn;0.0350|0.7497&plusmn;0.0043|0.6721&plusmn;0.0034|0.6121&plusmn;0.0035|0.6053&plusmn;0.0084|0.6514&plusmn;0.0045|
|libfm als|3.2605&plusmn;0.0080|0.7099&plusmn;0.0029|0.6635&plusmn;0.0016|0.6068&plusmn;0.0004|0.5972&plusmn;0.0002|0.6480&plusmn;0.0001|
|libfm mcmc|3.3610&plusmn;0.0438|0.7166&plusmn;0.0031|0.6684&plusmn;0.0018|0.6040&plusmn;0.0002|0.5941&plusmn;0.0002|0.6483&plusmn;0.0003|
|svdfeature|3.1251&plusmn;0.0044|0.7051&plusmn;0.0020|0.6583&plusmn;0.0018|0.5929&plusmn;0.0003|0.5811&plusmn;0.0003|0.6337&plusmn;0.0001|



# State-Of-The-Art

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



