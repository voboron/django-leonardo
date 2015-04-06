# -#- coding: utf-8 -#-

from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from feincms.module.page.models import Page
from leonardo.module.web.models import Widget


class PageTitleWidget(Widget):

    class Meta:
        abstract = True
        verbose_name = _("page title")
        verbose_name_plural = _('page titles')

    def render_content(self, options):
        page = Page.objects.best_match_for_path(
            options['request'].path, raise404=False)

        try:
            fragments = options['request']._feincms_fragments
        except:
            fragments = {}

        if fragments.has_key("_page_title"):
            title = fragments["_page_title"]
        else:
            title = None

        if fragments.has_key("_page_subtitle"):
            subtitle = fragments["_page_subtitle"]
        else:
            subtitle = None

        return render_to_string(self.template_name, {
            'widget': self,
            'request': options['request'],
            'page': page,
            'title': title,
            'subtitle': subtitle,
        })