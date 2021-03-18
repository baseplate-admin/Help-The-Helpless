from wagtail.core import blocks


class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    class Meta:  # noqa
        template = "about_blog/rich_text_block.html"
        icon = "doc-full"
        label = "Full RichText"
