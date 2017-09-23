import logging

from serp import SERP
from serp.types import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


erp = SERP();
erp.connect('demo.sqlite');

logger.debug(erp.documents['product_found'].human_name)
logger.debug(len(erp.documents['product_found']))
logger.debug(erp.catalogs['markets'].human_name)
logger.debug(len(erp.catalogs['markets']))
logger.debug(erp.documents['product_found'].get_by_id(1))

#
# Demo: create table
#

erp.documents.create(
    'reserve',

    valid_until = Datetime,

    items = Table(
        item = CatRef('items'),
        amount = Int
    ),

    comments = Table(
        comment = String,
    )
)

# import ipdb; ipdb.set_trace();
erp.documents.remove('reserve')
