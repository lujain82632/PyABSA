# -*- coding: utf-8 -*-
# file: rnac_trainer.py
# time: 02/11/2022 21:34
# author: yangheng <hy345@exeter.ac.uk>
# github: https://github.com/yangheng95
# GScholar: https://scholar.google.com/citations?user=NPq5a_0AAAAJ&hl=en
# ResearchGate: https://www.researchgate.net/profile/Heng-Yang-17/research
# Copyright (C) 2022. All Rights Reserved.

from typing import Union

from pyabsa import DeviceTypeOption, ModelSaveOption, TaskCodeOption, TaskNameOption
from pyabsa.framework.trainer_class.trainer_template import Trainer
from pyabsa.tasks.RNAClassification.configuration.rnac_configuration import RNACConfigManager
from pyabsa.tasks.RNAClassification.prediction.rna_classifier import RNAClassifier
from pyabsa.tasks.RNAClassification.instructor.rnac_instructor import RNACTrainingInstructor


class RNACTrainer(Trainer):

    def __init__(self, config: RNACConfigManager = None,
                 dataset=None,
                 from_checkpoint: str = None,
                 checkpoint_save_mode: int = ModelSaveOption.SAVE_MODEL_STATE_DICT,
                 auto_device: Union[bool, str] = DeviceTypeOption.AUTO,
                 path_to_save=None,
                 load_aug=False):
        """
        Init a trainer for trainer a APC, ATEPC, TC or TAD model, after trainer,
        you need to call load_trained_model() to get the trained model for inference.

        :param config: PyABSA.config.ConfigManager
        :param dataset: Dataset name, or a dataset_manager path, or a list of dataset_manager paths
        :param from_checkpoint: A checkpoint path to train based on
        :param checkpoint_save_mode: Save trained model to checkpoint,
                                     "checkpoint_save_mode=1" to save the state_dict,
                                     "checkpoint_save_mode=2" to save the whole model,
                                     "checkpoint_save_mode=3" to save the fine-tuned BERT,
                                     otherwise avoid saving checkpoint but return the trained model after trainer
        :param auto_device: True or False, otherwise 'allcuda', 'cuda:1', 'cpu' works
        :param path_to_save=None: Specify path to save checkpoints
        :param load_aug=False: Load the available augmentation dataset if any

        """
        super(RNACTrainer, self).__init__(config=config, dataset=dataset, from_checkpoint=from_checkpoint,
                                          checkpoint_save_mode=checkpoint_save_mode, auto_device=auto_device,
                                          path_to_save=path_to_save, load_aug=load_aug)

        self.training_instructor = RNACTrainingInstructor
        self.inference_model_class = RNAClassifier
        self.config.task_code = TaskCodeOption.RNASequenceClassification
        self.config.task_name = TaskNameOption[TaskCodeOption.RNASequenceClassification]

        self._run()