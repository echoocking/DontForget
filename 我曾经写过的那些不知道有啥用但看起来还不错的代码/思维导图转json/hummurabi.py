import re


def get_separate(words):
    """使用!给数据中的单词标记层次，并返回标记后的串行文本结构 """
    index = 1
    new_words = []
    for word in words:
        if word:
            new_words.append('!'*index+word)
        index += 1
    new_words.append('!')
    return ''.join(new_words)


def prepare_data(file_path):
    """将数据转为可处理的格式"""
    with open(file_path, 'r', encoding='utf-8') as datafile:
        data = ''
        for line in datafile.readlines():
            words = line.replace('\n', '').split(',')
            data += get_separate(words)
    return data


def find_by_level(level, nodes):
    level_objs = []
    for node in nodes:
        if node['level'] == level:
            level_objs.append(node)
    return level_objs


def find_by_id(id, nodes):
    for node in nodes:
        if node['id'] == id:
            return node


def find_parent(level, id, nodes):

    fake_parents = find_by_level(level-1, nodes)
    real_parent = 0
    sub = 0
    for parent in fake_parents:
        if parent['id'] < id:
            if fake_parents.index(parent) == 0 or id-parent['id'] < sub:
                sub = id-parent['id']
                real_parent = parent
    return real_parent


def find_childrenid(id, nodes):
    children_ids = []
    for node in nodes:
        # print(node, id)
        if node['parent'] == id:
            children_ids.append(node['id'])
    return children_ids


def create_json(node, childrens_ids, nodes):
    """

    :param node: 需要添加子节点的节点对象
    :param childrens_ids: @node 的子节点的id数组
    :param nodes: 整个图所有的节点对象，用于查找id对应的节点对象
    :return:
    """
    children_nodes = []
    for children_id in childrens_ids:
        children_nodes.append(find_by_id(children_id, nodes))
    node['children'] = children_nodes

    for children_node in children_nodes:
        create_json(children_node, children_node['childrenids'], nodes)


def adjust_json(node_title, nodes, new_json_obj):
    """
    调整create_json的结果为题目答案对应的格式
    :param node_title: 此次处理的node title
    :param nodes: @node_title 对应的children信息
    :param new_json_obj: 需要对号入座的存储位置。
    :return:
    """
    sub_title = {}
    for node in nodes:
        sub_title[node['title']] = []
    new_json_obj[node_title] = [sub_title]

    for sup_nodes in nodes:
        adjust_json(sup_nodes['title'], sup_nodes['children'], new_json_obj[node_title][0])


def csv2_json(file_path):
    data = prepare_data(file_path)
    pattern = '!+[^!]+(?=!)'
    swdt_words = re.findall(pattern, data)
    nodes = []
    # 遍历数组，将数组中每个元素创建为一个节点对象
    for word in swdt_words:
        word_obj = {}
        word_obj['id'] = swdt_words.index(word)
        word_obj['title'] = word.replace('!', '')
        word_obj['level'] = len(word) - len(word_obj['title'])
        if word_obj['level'] == 1:
            word_obj['parent'] = -1
        else:
            word_obj['parent'] = find_parent(word_obj['level'], word_obj['id'], nodes)['id']
        word_obj['childrenids'] = []
        nodes.append(word_obj)

    # 遍历数组，为每个节点补上子节点集合
    for node in nodes:
        node['childrenids'] = find_childrenid(node['id'], nodes)

    # 转化为json数组
    json_obj = {
        'title': '奴隶社会',
        'id': 0,
        'parent': 0,
        'level': 0,
        'childrenids': find_childrenid(0, nodes)
    }

    create_json(json_obj, json_obj['childrenids'], nodes)
    # 调整为答案所需格式
    adjust_json_obj = {'奴隶社会': []}
    adjust_json('奴隶社会', json_obj['children'], adjust_json_obj)
    import json
    print(json.dumps(adjust_json_obj, indent=4))
    return adjust_json_obj

result = csv2_json('data.csv')


