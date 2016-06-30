# state-of-the-art hulu
paper = "https://arxiv.org/abs/1605.09477"
code = "https://github.com/Ian09/CF-NADE"



out = "#state-of-the-art\n\n"

out += "## MovieLens 1M\n"
out += "|METHOD|TEST RMSE|\n"
out += "|:----|:----:|\n"
out += "|PMF (Dziugaite & Roy, 2015)|0.883|\n"
out += "|U-RBM (Sedhain et al., 2015)|0.881|\n"
out += "|U-AUTOREC (SEDHAIN ET AL., 2015)|0.874|\n"
out += "|LLORMA-GLOBAL (LEE ET AL., 2013)|0.865|\n"
out += "|I-RBM (Sedhain et al., 2015)|0.854|\n"
out += "|BIASMF (Sedhain et al., 2015)|0.845|\n"
out += "|NNMF (DZIUGAITE & ROY, 2015)|0.843|\n"
out += "|LLORMA-LOCAL (LEE ET AL., 2013)|0.833|\n"
out += "|I-AUTOREC (SEDHAIN ET AL., 2015)|0.831|\n"
out += "|U-CF-NADE-S (SINGLE LAYER)|0.850|\n"
out += "|U-CF-NADE-S (2 LAYERS )|0.845|\n"
out += "|I-CF-NADE-S (SINGLE LAYER)|0.830|\n"
out += "|I-CF-NADE-S (2 LAYERS)|0.829|\n"
out += "\n"

out += "## MovieLens 10M\n"
out += "|METHOD|TEST RMSE|\n"
out += "|:----|:----:|\n"
out += "|U-AUTOREC (SEDHAIN ET AL., 2015)|0.867|\n"
out += "|I-RBM (Sedhain et al., 2015)|0.825|\n"
out += "|U-RBM (Sedhain et al., 2015)|0.823|\n"
out += "|LLORMA-GLOBAL (LEE ET AL., 2013)|0.822|\n"
out += "|BIASMF (Sedhain et al., 2015)|0.803|\n"
out += "|LLORMA-LOCAL (LEE ET AL., 2013)|0.782|\n"
out += "|I-AUTOREC (SEDHAIN ET AL., 2015)|0.782|\n"
out += "|U-CF-NADE-S (SINGLE LAYER)|0.772|\n"
out += "|U-CF-NADE-S (2 LAYERS)|0.771|\n"
out += "\n"

out += "## Netflix\n"
out += "|METHOD|TEST RMSE|\n"
out += "|:----|:----:|\n"
out += "|LLORMA-GLOBAL (LEE ET AL., 2013)|0.874|\n"
out += "|U-RBM (Sedhain et al., 2015)|0.845|\n"
out += "|BIASMF (Sedhain et al., 2015)|0.844|\n"
out += "|LLORMA-LOCAL (LEE ET AL., 2013)|0.834|\n"
out += "|I-AUTOREC (SEDHAIN ET AL., 2015)|0.823|\n"
out += "|U-CF-NADE-S (SINGLE LAYER)|0.804|\n"
out += "|U-CF-NADE-S (2 LAYERS)|0.803|\n"
out += "\n\n\n"

df = open("paper.log", "w")
df.write(out)
df.close()


