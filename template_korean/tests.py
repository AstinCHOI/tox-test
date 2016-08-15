# -*- coding:utf-8 -*-

from django.test import TestCase


class TemplateKoreanTestCase(TestCase):
    def setUp(self):
        pass

    def test_test(self):
        self.assertEqual(1, 1)

    def test_korean_proofread(self):
        import korean
        result = korean.l10n.proofread(u"박현우(은)는 사람이다.")
        self.assertEqual(result, u"박현우는 사람이다.")

    def test_korean_proofread_fail(self):
        import korean
        result = korean.l10n.proofread(u"박현우(은)는 사람이다.")
        self.assertNotEqual(result, u"박현우은 사람이다.")

    def test_korean_proofread_tag(self):
        from django.template import Context, Template
        rendered = Template(
            '{% load proofread %}'
            '{{ string|proofread }}'
        ).render(Context({
            'string': u'박현우(은)는 밥(을)를 먹었다.',
        }))
        self.assertEqual(rendered, u'박현우는 밥을 먹었다.')

