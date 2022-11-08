# -*- coding: utf-8 -*-
# file: train_rna_classification.py
# time: 22/10/2022 16:36
# author: yangheng <hy345@exeter.ac.uk>
# github: https://github.com/yangheng95
# GScholar: https://scholar.google.com/citations?user=NPq5a_0AAAAJ&hl=en
# ResearchGate: https://www.researchgate.net/profile/Heng-Yang-17/research
# Copyright (C) 2021. All Rights Reserved.
import random

from pyabsa import RNAClassification as RNAC
from pyabsa.utils.data_utils.dataset_item import DatasetItem

config = RNAC.RNACConfigManager.get_rnac_config_glove()
config.model = RNAC.GloVeRNACModelList.LSTM
config.num_epoch = 10
config.pretrained_bert = 'rna_bpe_tokenizer'
config.evaluate_begin = 0
config.max_seq_len = 60
config.hidden_dim = 768
config.embed_dim = 768
config.cache_dataset = True
# config.cache_dataset = True
config.dropout = 0.5
config.num_lstm_layer = 1
config.do_lower_case = False
config.seed = [random.randint(0, 10000) for _ in range(1)]
config.log_step = -1
config.show_metric = True
config.l2reg = 0.001
config.save_last_ckpt_only = True
config.num_mhsa_layer = 1

dataset = DatasetItem('degrad')

# classifier = RNAC.RNACTrainer(config=config,
#                               dataset=dataset,
#                               checkpoint_save_mode=1,
#                               auto_device=True
#                               ).load_trained_model()

rnas = [
    'GTGCGATCGTTGATCTTGTGGCTTGTGAGCCGTCGGATTCCACGGAGAGGCGAGAGACAGCGAGGAAGTGGTCGAGGAGGATGAGGAATAGTGGGTTTGGAGCGGTGGGGTATAGTGATGAGGTGGCGGATGATGTCAGAGCTTTGTTGAGGAGATATAAAGAAGGTGTTTGGTCGATGGTACAGTGTCCTGATGCCGCCGGAATATTCC',
    'GTGCGATCGTTGATCTTGTGGCTTGTGAGCCGTCGGATTCCACGGAGAGGCGAGAGACAGCGAGGAAGTGGTCGAGGAGGATGAGGAATAGTGGGTTTGAGGCGGTGGGGTATAGTGATGAGGTGGCGGATGATGTCAGAGCTTTGTTGAGGAGATATAAAGAAGGTGTTTGGTCGATGGTACAGTGTCCTGATGCCGCCGGAATATTCC',
    'GTGCGATCGTTGATCTTGTGGCTTGTGAGCCGTCGGATTCCACGGAGAGGCGAGAGACAGCGAGGAAGTGGTCGAGGAGGATGAGGAATAGTGGGTTTGAAGCAGTAGGATATAGTGATGAGGTGGCGGATGATGTCAGAGCTTTGTTGAGGAGATATAAAGAAGGTGTTTGGTCGATGGTACAGTGTCCTGATGCCGCCGGAATATTCC',
    'GTGCGATCGTTGATCTTGTGGCTTGTGAGCCGTCGGATTCCACGGAGAGGCGAGAGACAGCGAGGAAGTGGTCGAGGAGGATGAGGAATAGTGAATTTGAAGCAGTAGAATATAGTGATGAGGTGGCGGATGATGTCAGAGCTTTGTTGAGGAGATATAAAGAAGGTGTTTGGTCGATGGTACAGTGTCCTGATGCCGCCGGAATATTCC',
    'TTGATCTTGTGGCTTGTGAGCCGTCGGATTCCACGGAGAGGCGAGAGACAGCGAGGAAGTGGTCGAGGAGGATGAGGAATAGTGAATTTGAAGCAGTAGAATATAGTGATGAGGTGGCGGATGATGTCAGAGCTTTGTTGAGGAGATATAAAGAAGGTGTTTGGTCGATGGTACAGTGTCCTGATGCCGCCGGAATATTCC'
]
classifier = RNAC.RNAClassifier('lstm_degrad_acc_85.26_f1_84.62')
for rna in rnas:
    classifier.predict(rna + '$LABEL$')

# classifier.batch_predict(dataset)
