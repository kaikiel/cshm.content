# -*- coding: utf-8 -*-
from cshm.content.content.trainingcenter import ITrainingcenter  # NOQA E501
from cshm.content.testing import CSHM_CONTENT_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName


class TrainingcenterIntegrationTest(unittest.TestCase):

    layer = CSHM_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_trainingcenter_schema(self):
        fti = queryUtility(IDexterityFTI, name='TrainingCenter')
        schema = fti.lookupSchema()
        self.assertEqual(ITrainingcenter, schema)

    def test_ct_trainingcenter_fti(self):
        fti = queryUtility(IDexterityFTI, name='TrainingCenter')
        self.assertTrue(fti)

    def test_ct_trainingcenter_factory(self):
        fti = queryUtility(IDexterityFTI, name='TrainingCenter')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ITrainingcenter.providedBy(obj),
            u'ITrainingcenter not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_trainingcenter_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='TrainingCenter',
            id='trainingcenter',
        )
        self.assertTrue(
            ITrainingcenter.providedBy(obj),
            u'ITrainingcenter not provided by {0}!'.format(
                obj.id,
            ),
        )
