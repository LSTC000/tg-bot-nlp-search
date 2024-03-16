from ..core import CoreService
from .utils import NLPServiceUtils


class NLPService(CoreService):
    utils: NLPServiceUtils = NLPServiceUtils()
