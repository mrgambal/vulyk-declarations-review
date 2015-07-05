# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from vulyk.models.task_types import AbstractTaskType

from vulyk_declarations_review.models.tasks import ReviewAnswer, ReviewTask


class ReviewTaskType(AbstractTaskType):

    """
    Review Task to work with Vulyk.
    """
    answer_model = ReviewAnswer
    task_model = ReviewTask

    name = 'Редактирование оцифрованных деклараций'
    description = 'Вычитка и корректировка результатов оцифровки деклараций'

    template = 'base.html'
    helptext_template = 'help.html'
    type_name = 'review_task'

    redundancy = 1

    JS_ASSETS = ['static/scripts/base.js']

    CSS_ASSETS = [
        'static/styles/base.css',
        'static/styles/bootstrap-select.css']
