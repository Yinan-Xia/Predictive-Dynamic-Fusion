#!/usr/bin/env python3
#
# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#

from .bert import BertClf
from .bow import GloveBowClf
from .concat_bert import MultimodalConcatBertClf
from .concat_bow import  MultimodalConcatBowClf
from .image import ImageClf
from .mmbt import MultimodalBertClf
from .latefusion_pdf import MultimodalLateFusionClf_pdf
MODELS = {
    "bert": BertClf,
    "bow": GloveBowClf,
    "concatbow": MultimodalConcatBowClf,
    "concatbert": MultimodalConcatBertClf,
    "img": ImageClf,
    "mmbt": MultimodalBertClf,
    'latefusion_pdf':MultimodalLateFusionClf_pdf
}


def get_model(args):
    # print(args.model)
    return MODELS[args.model](args)
