# Generated by Django 3.0.2 on 2021-10-18 16:19

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import modelcluster.contrib.taggit
import modelcluster.fields
import streams.blocks
import wagtail.contrib.routable_page.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaintingCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
            ],
            options={
                'verbose_name': 'Painting Category',
                'verbose_name_plural': 'Painting Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PaintingDetailPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('date', models.DateField(blank=True, null=True)),
                ('width', models.FloatField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('description', wagtail.core.fields.StreamField([('simple_richtext', streams.blocks.SimpleRichtextBlock())], blank=True, null=True)),
                ('links', wagtail.core.fields.StreamField([('links', wagtail.core.blocks.StructBlock([('button_title', wagtail.core.blocks.CharBlock(max_length=60, required=False)), ('button_text', streams.blocks.RichtextBlock(features=['bold', 'italic'], required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(help_text='If selected, this url will be used first', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If added, this url will be used secondarily to the button page', required=False))], blank=True, null=True))], blank=True, null=True)),
                ('initial_inventory', wagtail.core.fields.StreamField([('dbreference', wagtail.core.blocks.CharBlock(blank=True, default='a', help_text='Entry from initial Excel Inventory by JMC, for internal needs only', max_length=50, null=True)), ('remark', wagtail.core.blocks.CharBlock(blank=True, default='a', help_text='Entry from initial Excel Inventory by JMC, for internal needs only', max_length=150, null=True)), ('signature', wagtail.core.blocks.BooleanBlock(blank=True, detault='Yes', null=True))], blank=True, null=True)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('painter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PaintingIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('subtitle', wagtail.core.fields.RichTextField(blank=True, help_text='Catchy, short informative description of the page', max_length=250, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='PaintingLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
            ],
            options={
                'verbose_name': 'Painting Location',
                'verbose_name_plural': 'Painting Locations',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PaintingMedium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
            ],
            options={
                'verbose_name': 'Paining Medium',
                'verbose_name_plural': 'Painting Mediums',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PaintingSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
            ],
            options={
                'verbose_name': 'Paining Support',
                'verbose_name_plural': 'Painting Supports',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PaintingPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='catalog.PaintingDetailPage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalog_paintingpagetag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='paintingdetailpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='catalog.PaintingPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.CreateModel(
            name='PaintingPagePaintingSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='supports', to='catalog.PaintingDetailPage')),
                ('painting_support', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_pages', to='catalog.PaintingSupport')),
            ],
            options={
                'unique_together': {('page', 'painting_support')},
            },
        ),
        migrations.CreateModel(
            name='PaintingPagePaintingMedium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='mediums', to='catalog.PaintingDetailPage')),
                ('painting_medium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_pages', to='catalog.PaintingMedium')),
            ],
            options={
                'unique_together': {('page', 'painting_medium')},
            },
        ),
        migrations.CreateModel(
            name='PaintingPagePaintingLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='catalog.PaintingDetailPage')),
                ('painting_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_pages', to='catalog.PaintingLocation')),
            ],
            options={
                'unique_together': {('page', 'painting_location')},
            },
        ),
        migrations.CreateModel(
            name='PaintingPagePaintingCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='catalog.PaintingDetailPage')),
                ('painting_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_pages', to='catalog.PaintingCategory')),
            ],
            options={
                'unique_together': {('page', 'painting_category')},
            },
        ),
    ]
