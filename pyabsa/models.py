# -*- coding: utf-8 -*-
# file: models.py
# time: 2021/6/11 0011
# author: yangheng <yangheng@m.scnu.edu.cn>
# github: https://github.com/yangheng95
# Copyright (C) 2021. All Rights Reserved.
import os.path

from google_drive_downloader import GoogleDriveDownloader as gdd


def download_pretrained_model(task='apc', language='chinese', archive_path='', model_name='any_model'):
    tmp_dir = '{}_{}_TRAINED_MODEL'.format(task.upper(), language.upper())
    dest_path = os.path.join('.', tmp_dir)
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    if len(os.listdir(dest_path)):
        return dest_path
    save_path = os.path.join(dest_path, '{}.zip'.format(model_name))
    try:
        gdd.download_file_from_google_drive(file_id=archive_path,
                                            dest_path=save_path,
                                            unzip=True)
    except:
        raise ConnectionError('Download failed, you can download the trained model manually at: {}, ' +
                              'it is recommended to train the model on your custom dataset'.format(
                                  'https://drive.google.com/drive/folders/1yiMTucHKy2hAx945lgzhvb9QeHvJrStC'))
    os.remove(save_path)
    return dest_path


class APCTrainedModelManger:
    ChineseModel = '1dPvXgQIQn3c2VkWjW3iE4o_A7oWfjnWv'
    EnglishModel = '1QyRM3RrnCjz293G3pol9jJM8CShAZuof'
    MultilingualModel = ''

    @staticmethod
    def get_Chinese_APC_trained_model(model_name=''):
        return download_pretrained_model(task='apc',
                                         language='chinese',
                                         archive_path=APCTrainedModelManger.ChineseModel,
                                         model_name=model_name)

    @staticmethod
    def get_English_APC_trained_model(model_name=''):
        return download_pretrained_model(task='apc',
                                         language='english',
                                         archive_path=APCTrainedModelManger.EnglishModel,
                                         model_name=model_name)

    @staticmethod
    def get_Multilingual_APC_trained_model(model_name=''):
        return download_pretrained_model(task='apc',
                                         language='multilingual',
                                         archive_path=APCTrainedModelManger.MultilingualModel,
                                         model_name=model_name)


class ATEPCTrainedModelManager:
    ChineseModel = '19VdszKYWTVL4exaSTU5zl3ueP5FNbKeJ'
    EnglishModel = ''
    MultilingualModel = ''

    @staticmethod
    def get_Chinese_ATEPC_trained_model(model_name=''):
        return download_pretrained_model(task='atepc',
                                         language='chinese',
                                         archive_path=ATEPCTrainedModelManager.ChineseModel,
                                         model_name=model_name)

    @staticmethod
    def get_English_ATEPC_trained_model(model_name=''):
        return download_pretrained_model(task='atepc',
                                         language='english',
                                         archive_path=ATEPCTrainedModelManager.EnglishModel,
                                         model_name=model_name)

    @staticmethod
    def get_Multilingual_ATEPC_trained_model(model_name=''):
        return download_pretrained_model(task='atepc',
                                         language='multilingual',
                                         archive_path=ATEPCTrainedModelManager.MultilingualModel,
                                         model_name=model_name)


class APCModelList:
    BERT_BASE = 'bert_base'
    BERT_SPC = 'bert_spc'
    LCF_BERT = 'lcf_bert'
    LCFS_BERT = 'lcfs_bert'
    SLIDE_LCF_BERT = 'slide_lcf_bert'
    SLIDE_LCFS_BERT = 'slide_lcfs_bert'
    LCA_BERT = 'lca_bert'


class ATEPCModelList:
    BERT_BASE = 'bert_base'
    LCF_ATEPC = 'lcf_atepc'