import towhee

from logs import LOGGER


class Resnet50:
    """
    Say something about the ExampleCalass...

    Args:
        args_0 (`type`):
        ...
    """

    @staticmethod
    def resnet50_extract_feat(img_path):
        try:
            feat = towhee.glob(img_path) \
                .image_decode() \
                .image_embedding.timm(model_name='resnet50') \
                .tensor_normalize() \
                .to_list()
            return feat[0] if feat else None
        except Exception as e:
            LOGGER.exception(e)
            LOGGER.error(f"Error with resnet50_extract_feat from image {img_path}.")
