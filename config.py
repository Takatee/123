from pathlib import Path
from typing import List, Literal, Optional, Union

from nonebot import get_driver
from pydantic import BaseModel, Extra


class Config(BaseModel, extra=Extra.ignore):
    chatgpt_session_token: str = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..dEZKOzRzhrHgJQmW.CdhTYSlr15q30OcBhAREPAYRo-C4LQA0mk-5P41Au-sfoO81sTjSLwppv1hKc8r_fhvS4jN_7OgVA7r-cs5nLzcwyHRW5wLUGKHXwuAhYeFH3Efm3Wghq6wciQXjlr1jP0KidGJWRKrnHOLfvstmRqgAZ0dK9auEYznbryMenClheIh4lSsXfV2Pr9CbmbVK2CqoHPrrPs0hR89b-SZSsbeaCDZUmXnpqJN2pgZSuvTRAb5ot3EW4TqvU67EiCvXldfhKuNdpNxsjYw0_r-AoA515MS20uEfO0AKyFn0gj9s7928d2o3mWHHtPbwzVTk_iutuWY_lKXgjcx0v0-WdyLcIneFYXtVSQ_ir3FgK_reTxFSM24D0gptYRgKJwO5yxP2vJYVW_Fe7LGL5O5iMa1lJCYwjnYF8rauMfSysosJXvVGeSVqFzGajzwCLLKq0T4VXNzHIp9Nd_xnrwoyfNLu8vfff_mCl-XvY0iVOn2K7Qc_bLqV9XgXpCuYbxpUYB0Y7QOTeY_iIaCCUQj7Jn2mvIRgm7mReRbJCw6z-0zk0V9_iElgpWzOX32OR3O7ze2wXSncLm9EVU-fc7pxmKdlvcSYi7aYsA4MC-VJVnJOs729T8pPx9gGz4LmatCXTowdyPJooNE2F-RLhGbQ0J3Cirvlg1g57H01Et1_eNqd622joiBz4IHWYngpJEp1duOCqwguCFEy9T9NL6V4czd4LfObdLXO88CrICOTmfrQKzfvzmfi41OtASlNFWvpxL08Xr2xmTbdyHEqeciBJW44U9YA-tyPdD1gnVZWLwZ_LavdmnJsINsVqHxj1wlbmlOewB1k22e8dpCcYQyW2I46fnTt_H7Lmi_AyO2kTeCqeH5V-etcRwruM2bOKDw9AP_r4KCVMPF9iugSpKjHC2Z56W2-piAcBi1cuJ1AlJCKstmthoVKNZRGavT9jg76AA5ubMrq_I5VVBzhsFt6hPyg4PHDoqgwVVde_b_RyzODV_HidGKxAuV_JhZPzxplb0wtp5GlHW-iLY93_HIaoH_17q7pwy47ja8a_MYuCA45pmXCtC8_2Y5joNRka0xhw0vRX6F2jj8Tw7MbDYIprRZLKyogmCXE4PvCFsxoAYHJ6_az3juOmbvSMqNsfwfvwpZvy-gV805Hh7_7keahYk3TVxGKNrNNTwpV47HGhxgbqkXU9BsFQ633SsFESeEDiBKTjfCzWhnpd3nQijEAGBbj1GSwDgMyrRlEttqN1sq5PRlsTvfRRxUmHJnA8K09PURTgGZhhHaed2Hn-G6ckbBICUBL119h-1L_JCzpApY2BCvqAFZaY8EIn-Zu1iSyTA04Mxg1NR5SsFcaBqwgKtvhxfvn__pn3M1XqcmBJv8RRu8QiUCv9RAT5S5kZyr6qQPWDXb1fBX9vZCIXl87fzzLOQ-8A0xsbR89nKObxeDfb2GZD8MEffSb6g5SH_DPBdUW9Awx3iMPNM0v5YpsQMSG8J4IRVkWs0R9X3N7btRMMqZqIPUYbZSTlDVF-0xqMz7Dtjo73nfqB7ODtI_eUjzVIuH1NSJGBBQeKjj8LSdK8XemAfnE8He2kSeylcVeZrI3POCz744r1eWLaTiJ0_sqcUJWpBgvdL_y08vkOxX4lyXLVYDKLzmbEjqtYHO4HzHh4kSOTuJzv8hUrfKfejbtMQibfFKbIy0Ss-nsrY-LDkNWq2F1aOzQptQhhAOzZoGUHWpPKL4BSC81x9ybHB_AQRJklcRotRiXDhrJLDoBrA5cwWP1Eg1W3ZF_eLanxg4ecyFd0vpvB-2v2kx9h8pJOaHOANNPVeyX8tmbVre3pqFgKmzCoalQZdWA1A_h-iiNVtjfrPxWulE_vhAQQVMFtvesCuJmXDpGj4sxkR9dT7JWff2tWtG4BD1_cROdJZ4-BQI-OWWsB1pWv2A365Yg5g9Ed2C6G5zxlLg2J9HZiOH03ARFexXcxoVtUvY-6CkXq0Y9E2WyvCN2mkFvd3HjFILlQQ0RVeMss_eZCbllVPCUb2zmtMX-MNOc6GyY0oag3RnJdxTuUu5Pfxgl4_U388eLwqqwQ8fuYuVEqkYiMJlZw2YMQPkd8BrQ_viUkTBozWHexU3QpzkNLW6BIc5kB5Lsm-Xx928n3-Twwg-krBpRlq9zMhcYSYsgLNn9JDvmTT84w2E5UJ3JGzlYK-HCYoZ1H8E_x6jgqigDFD1e-L69ya2rMZJxyViCNP_Gr6Pd31dNmBtqQQiRgGGlamB4ojpNYgcJF4Mm9u990xy_Z0_OZ3YBRArVVmJ-l8q0IohLB2u4vLqbyGBigonSHQmlrXhjVjl8Q3o4lEOB7zC48z8uStYPKigG8u1giW05OfwTeIuY4Wt2wxzcVDhrqH_Gv_eF4mBpeGdpoESqd_5X3cPDXeiELfTJzFMeJJeAHXDxSe4xcbWsaVxtN58xO-Aw9Iz4UIp_bZY-lRURm_NWqeB9sSsE9B7levP-KBvO9kbqFWIkwgMigHacNpMjJ8ZCn7aAoh7h5uvlxUOImPro4JXi_2zxDeWNNFsltZ92pJFakl5wDyHa6V1loRCottyZXG_i34o0-3EiZLQNKq6yZeAlwG5C76cknvR95oF0HPNI9Zd0MJJzUj5CWBpaYDiPWcudqzYr3pJit9jSTq9A.32GbdQFKZOtuOktKrkWEbg"
    chatgpt_account: str = ""
    chatgpt_password: str = ""
    chatgpt_cd_time: int = 60
    chatgpt_proxies: Optional[str] = None
    chatgpt_refresh_interval: int = 30
    chatgpt_command: Union[str, List[str]] = ""
    chatgpt_to_me: bool = True
    chatgpt_timeout: int = 30
    chatgpt_api: str = "https://chat.openai.com/"
    chatgpt_image: bool = False
    chatgpt_image_width: int = 500
    chatgpt_priority: int = 999
    chatgpt_block: bool = True
    chatgpt_private: bool = True
    chatgpt_scope: Literal["private", "public"] = "private"
    chatgpt_data: Path = Path(__file__).parent
    chatgpt_max_rollback: int = 5
    chatgpt_detailed_error: bool = False


config = Config.parse_obj(get_driver().config)
