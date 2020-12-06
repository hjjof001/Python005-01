import requests
import re
import json
import time

entry = 'https://www.zhihu.com/question/46852043/answer/105218389'
useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
answers_url = 'https://www.zhihu.com/api/v4/questions/46852043/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics%3Bsettings.table_of_content.enabled%3B&offset=3&limit=15&sort_by=default&platform=desktop'
# https://www.zhihu.com/api/v4/questions/46852043/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bsettings.table_of_content.enabled%3B&limit=5&offset=8&platform=desktop&sort_by=default
titleRegex = r'<title data-react-helmet="true">(.*?) - 知乎</title>'
answerRegex = r'itemProp="answerCount" content="(\d+)"/>'


if __name__ == "__main__":
    session = requests.session()
    header = {
        'User-Agent': useragent
    }

    raw_result = session.get(url=entry,headers=header)
    print(raw_result.text)
    title_search = re.compile(titleRegex)
    title = title_search.findall(raw_result.text)[0]
    print(f"Title: {title}")

    ans_search = re.compile(answerRegex)
    answers_count = ans_search.findall(raw_result.text)[0]
    print(f"Answer's count: {answers_count}")

    raw_result = session.get(url=answers_url,headers=header)
    json_data = json.loads(raw_result.text)

    answers = json_data['data']
    print(f'Got {len(answers)} answers')
    for answer in answers:
        # print(answer)
        with open("answer_cache.txt", "a", encoding='utf-8') as f:
            f.write(answer['author']['name'])
            f.write('\n')
            f.writelines(answer['content'])
            f.write('\n')
        time.sleep(1)
        print(answer['author']['name'])