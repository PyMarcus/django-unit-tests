from django.test import TestCase
from model_mommy import mommy


class ServicesTestCase(TestCase):
    def setUp(self) -> None:
        self.service = mommy.make('Services')

    def test_str(self) -> None:
        self.assertEquals(str(self.service), self.service.service)


class TeamTestCase(TestCase):
    def setUp(self) -> None:
        self.team = mommy.make('Team')

    def test_str(self) -> None:
        self.assertEquals(str(self.team), self.team.name)


class ProfissionTestCase(TestCase):
    def setUp(self) -> None:
        self.profission = mommy.make('Profission')

    def test_str(self) -> None:
        self.assertEquals(str(self.profission), self.profission.profission)
