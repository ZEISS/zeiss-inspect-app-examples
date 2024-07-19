# -*- coding: utf-8 -*-

import gom

from enum import Enum


# ----------------------------------------------------------------------------------
# Constants
# ----------------------------------------------------------------------------------

#
# Type of evaluation
#
class EvaluationType(Enum):
    Anova_2 = "ANOVA-2"
    Anova_3 = "ANOVA-3"
    Arm = "ARM"
    Export = "Export"


#
# Id addressing the element object families to be able to access the right tokens. These
# ids are used during table template import as some kind of jokers for whole element groups.
#
Type_Inspection = '!scalar_checks'
Type_GDAT = '!gdt'
Type_Picker = '!picker'
Type_TwoPointInspection = 'inspection_dimension_two_point'

#
# Element keyword set for each automatically created element
#
automatically_created_tag = 'msa_automatically_created'

#
# Value elements used to tag appraiser, part and trial in each stage and the global sigma value
#
appraiser_tag = 'msa_appraiser'
part_tag = 'msa_part'
trial_tag = 'msa_trial'
sigma_tag = 'msa_sigma'

#
# Name of the stage range representing all stages
#
all_stages_range_name = 'All stages'

#
# Default sigma factor
#
default_sigma_factor = 6.0
