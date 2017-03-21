if [ ! -d jester ]; then
    mkdir jester
    
    if [ ! -f jester_dataset_1_1.zip ]; then
        echo "download jester_dataset_1_1.zip ..."
        wget http://eigentaste.berkeley.edu/dataset/jester_dataset_1_1.zip
    fi
    echo "uncompress jester_dataset_1_1.zip ..."
    unzip -o -d jester jester_dataset_1_1.zip
    
    if [ ! -f jester_dataset_1_2.zip ]; then
        echo "download jester_dataset_1_2.zip ..."
        wget http://eigentaste.berkeley.edu/dataset/jester_dataset_1_2.zip
    fi
    echo "uncompress jester_dataset_1_2.zip ..."
    unzip -o -d jester jester_dataset_1_2.zip
    
    if [ ! -f jester_dataset_1_3.zip ]; then
        echo "download jester_dataset_1_3.zip ..."
        wget http://eigentaste.berkeley.edu/dataset/jester_dataset_1_3.zip
    fi
    echo "uncompress jester_dataset_1_3.zip ..."
    unzip -o -d jester jester_dataset_1_3.zip
    
    if [ ! -f jester_dataset_1_joke_texts.zip ]; then
        echo "jester_dataset_1_joke_texts.zip ..."
        wget http://eigentaste.berkeley.edu/dataset/jester_dataset_1_joke_texts.zip
    fi
    echo "uncompress jester_dataset_1_joke_texts.zip ..."
    unzip -o -d jester jester_dataset_1_joke_texts.zip
fi

if [ ! -d ml-100k ]; then
    if [ ! -f ml-100k.zip ]; then
        echo "download ml-100k.zip ..."
        wget http://files.grouplens.org/datasets/movielens/ml-100k.zip
    fi
    echo "uncompress ml-100k.zip ..."
    unzip ml-100k.zip
fi

if [ ! -d ml-1m ]; then
    if [ ! -f ml-1m.zip ]; then
        echo "download ml-1m.zip ..."
        wget http://files.grouplens.org/datasets/movielens/ml-1m.zip
    fi
    echo "uncompress ml-1m.zip ..."
    unzip ml-1m.zip
fi

if [ ! -d ml-10M100K ]; then
    if [ ! -f ml-10m.zip ]; then
        echo "download ml-10m.zip ..."
        wget http://files.grouplens.org/datasets/movielens/ml-10m.zip
    fi
    echo "uncompress ml-10m.zip ..."
    unzip ml-10m.zip
fi

if [ ! -d ml-20m ]; then
    if [ ! -f ml-20m.zip ]; then
        echo "download ml-20m.zip ..."
        wget http://files.grouplens.org/datasets/movielens/ml-20m.zip
    fi
    echo "uncompress ml-20m.zip ..."
    unzip ml-20m.zip
fi

if [ ! -d download ]; then
    if [ ! -f nf_prize_dataset.tar.gz ]; then
        echo "download nf_prize_dataset.tar.gz ..."
        aria2c --seed-time 0 http://academictorrents.com/download/9b13183dc4d60676b773c9e2cd6de5e5542cee9a.torrent
        rm 9b13183dc4d60676b773c9e2cd6de5e5542cee9a.torrent
    fi
    echo "uncompress nf_prize_dataset.tar.gz ..."
    tar -zxvf nf_prize_dataset.tar.gz
    cd download
    tar -xvf training_set.tar
    cd ..
fi
