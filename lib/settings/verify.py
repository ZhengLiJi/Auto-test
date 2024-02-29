import json

from pactverify.matchers import Matcher, Like, EachLike, Enum, Term, PactVerify

from lib.settings.logger import log


class Verify:
    """校验"""

    @staticmethod
    def verify_response(act_rsp, exp_rsp, verify_mode=0, hard_mode=True, assert_mode=True):
        """
        校验响应数据
        act_rsp: 实际返回的数据
        exp_rsp: 期望返回的数据
        verify_mode: 验证模式 [Matcher, Like, EachLike, Enum, Term]
        hard_mode: 是否开启严格校验
        assert_mode：是否打开断言开关
        """
        if assert_mode:
            log.info(f"act_rsp: \n{json.dumps(act_rsp, ensure_ascii=False)}")
            log.info(f"exp_rsp: \n{json.dumps(exp_rsp, ensure_ascii=False)}")
            verify_type_lst = [Matcher, Like, EachLike, Enum, Term]
            verify_mode = 1 if verify_mode not in range(len(verify_type_lst)) else verify_mode
            verify_mode = verify_type_lst[verify_mode]
            exp_format = verify_mode(exp_rsp)
            pv = PactVerify(exp_format, hard_mode=hard_mode)
            pv.verify(act_rsp)
            if pv.verify_result:
                log.info("verify passed")
                verify_info = ""
            else:
                log.error("verify failed")
                verify_info = json.dumps(pv.verify_info, indent=4, ensure_ascii=False)
                log.error(verify_info)
            assert pv.verify_result, verify_info
        else:
            return None
