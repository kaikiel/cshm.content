# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from z3c.relationfield.schema import RelationList, RelationChoice
from plone.app.vocabularies.catalog import CatalogSource
from zope import schema
from zope.interface import implementer
from cshm.content import _


class ICourse(model.Schema):
    """ Marker interface and Dexterity Python Schema for Course
    """

    # fieldset('CourseDetail', fields=[])
    reTrainingBaseOn = schema.TextLine(
        title=_(u'Retraining Base On'),
        required=False,
    )

    reTrainingCourse = RelationChoice(
        title=_(u"Retrainging Course"),
        required=False,
        source=CatalogSource(Type='Course')
    )

    handbookTitle = schema.TextLine(
        title=_(u'Handbook Title'),
        required=True,
    )

    courseHours = schema.Int(
        title=_(u"Course Hours"),
        default=0,
        description=_(u"If 0, asking for phone"),
        required=True,
    )

    courseFee = schema.Int(
        title=_(u"Course Fee"),
        default=0,
        description=_(u"If 0, asking for phone"),
        required=True,
    )

    courseRequired = RichText(
        title=_(u"Course Required"),
        required=False,
    )

    trainee = RichText(
        title=_(u"Trainee"),
        required=False,
    )

    courseScope = schema.TextLine(
        title=_(u"Course Scope"),
        required=False,
    )

    courseEffective = schema.TextLine(
        title=_(u"Course Effective"),
        required=False,
    )

    introduction = RichText(
        title=_(u"Introduction"),
        required=False,
    )

    otherNote = RichText(
        title=_(u"Other Note"),
        required=False,
    )

    certificateCode = schema.TextLine(
        title=_(u"Certificate Code"),
        required=False,
    )

    sampleTitle = schema.TextLine(
        title=_(u"Sample Title"),
        required=False,
    )

    reTrainingYears = schema.Int(
        title=_(u"Retraining Years"),
        default=0,
        description=_(u"If 0, no need retraining."),
        required=True,
    )

    licenseType = schema.TextLine(
        title=_(u"License Type"),
        required=True,
    )

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    # url = schema.URI(
    #     title=_(u'Link'),
    #     required=False
    # )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )

    # advertisement = namedfile.NamedBlobImage(
    #     title=_(u'Advertisement (Gold-sponsors and above)'),
    #     required=False,
    # )

    # directives.read_permission(notes='cmf.ManagePortal')
    # directives.write_permission(notes='cmf.ManagePortal')
    # notes = RichText(
    #     title=_(u'Secret Notes (only for site-admins)'),
    #     required=False
    # )


@implementer(ICourse)
class Course(Container):
    """
    """
