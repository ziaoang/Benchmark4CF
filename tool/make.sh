# libmf
tar -zxvf libmf-2.01.tar.gz
cd libmf-2.01
make
cd ..

# libfm
tar -zxvf libfm-1.42.src.tar.gz
cd libfm-1.42.src
make
cd ..

# svdfeature
tar -zxvf Svdfeature-1.2.2.tar.gz
cd svdfeature-1.2.2
make
cd tools
make
cd ..
cd ..

