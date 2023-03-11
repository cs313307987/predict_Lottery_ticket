# -*- coding: utf-8 -*-
"""
Author: BigCat
"""
import os

ball_name = [
    ("红球", "red"),
    ("蓝球", "blue")
]

data_file_name = "data.csv"

name_path = {
    "ssq": {
        "name": "双色球",
        "path": "data/ssq/"
    },
    "dlt": {
        "name": "大乐透",
        "path": "data/dlt/"
    }
}

model_path = os.getcwd() + "/model/"

model_args = {
    "ssq": {
        "model_args": {
            "windows_size": 3,
            "batch_size": 1,
            "sequence_len": 6,
            "red_n_class": 33,
            "red_epochs": 80,
            "red_embedding_size": 640,
            "red_hidden_size": 640,
            "red_layer_size": 30,
            "blue_n_class": 16,
            "blue_epochs": 80,
            "blue_embedding_size": 640,
            "blue_hidden_size": 640,
            "blue_layer_size": 20
        },
        "train_args": {
            "red_learning_rate": 0.01,
            "red_beta1": 0.9,
            "red_beta2": 0.999,
            "red_epsilon": 1e-08,
            "blue_learning_rate": 0.01,
            "blue_beta1": 0.9,
            "blue_beta2": 0.999,
            "blue_epsilon": 1e-08
        },
        "path": {
            "red": model_path + "/ssq/red_ball_model/",
            "blue": model_path + "/ssq/blue_ball_model/"
        }
    },
    "dlt": {
        "model_args": {
            "windows_size": 3,
            "batch_size": 1,
            "red_sequence_len": 5,
            "red_n_class": 36,
            "red_epochs": 8,
            "red_embedding_size": 640,
            "red_hidden_size": 640,
            "red_layer_size": 30,
            "blue_sequence_len": 2,
            "blue_n_class": 13,
            "blue_epochs": 80,
            "blue_embedding_size": 640,
            "blue_hidden_size": 640,
            "blue_layer_size": 20
        },
        "train_args": {
            "red_learning_rate": 0.01,
            "red_beta1": 0.9,
            "red_beta2": 0.999,
            "red_epsilon": 1e-08,
            "blue_learning_rate": 0.01,
            "blue_beta1": 0.9,
            "blue_beta2": 0.999,
            "blue_epsilon": 1e-08
        },
        "path": {
            "red": model_path + "/dlt/red_ball_model/",
            "blue": model_path + "/dlt/blue_ball_model/"
        }
    }
}

# 模型名
pred_key_name = "key_name.json"
red_ball_model_name = "red_ball_model"
blue_ball_model_name = "blue_ball_model"
extension = "ckpt"
