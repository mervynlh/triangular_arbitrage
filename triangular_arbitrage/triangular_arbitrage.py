# -*- coding: utf-8 -*-


def arbitrage(q_list, p_list, args=[0.0, 0.0], sli_list=[0.0, 0.0, 0.0], fee_list=[0.002, 0.002, 0.002], coin='end'):
    """
    example:
    htusdt - hteth*ethusdt
    :param q_list: q1代表ht的数量，q2代表eth的数量，q3代表usdt的数量 保证 q1*p1<=q3
    :param p_list:  p1代表ht/usdt的价格，p2代表hteth的价格，p3代表ethusdt的价格
    :param args: args_1 代表 阀值，args_2 代表 htusdt begin ht 的交易个数
    :param sli_list: 滑点list
    :param fee_list: 手续费list
    :param coin: begin mid end ，分别代表三个币的位置 htusdt hteth ethusdt  ht-begin eth-mid usdt-end
    :return: transaction-0 ht/usdt交易的个数，transaction-1 hteth交易的个数，transaction-2 ethusdt交易的个数 ,flag ==0 ,没有数据返回
    """
    flag = 1
    transaction = []
    p1 = p_list[0]
    p2 = p_list[1]
    p3 = p_list[2]
    q1 = args[1]
    param1 = args[0]
    sli_1 = sli_list[0]
    sli_2 = sli_list[1]
    sli_3 = sli_list[2]
    fee_1 = fee_list[0]
    fee_2 = fee_list[1]
    fee_3 = fee_list[2]
    positive = p1 * (1 - sli_1) * (1-fee_1) - p2 * (1 + sli_2) / (1 - fee_2) * p3 * (1 + sli_3) / (1 - fee_3)
    negative = p1 * (1 + sli_1) / (1 - fee_1) - p2 * (1 - sli_2) * (1 - fee_2) * p3 * (1 - sli_3) * (1 - fee_3)
    if positive > param1:
        # print('positive:', positive)
        p1 = p_list[0] * (1 - sli_1) * (1 - fee_1)
        p2 = p_list[1] * (1 + sli_2) / (1 - fee_2)
        p3 = p_list[2] * (1 + sli_3) / (1 - fee_3)
        transaction, count = transaction_q(p1, p2, p3, q1, coin=coin, d_value=1)
        if coin == 'begin':
            q_list[0] += count
        elif coin == 'end':
            q_list[2] += count
        else:
            q_list[1] += count
    elif negative < -param1:
        # print('negative:', negative)
        p1 = p_list[0] * (1 + sli_1) / (1 - fee_1)
        p2 = p_list[1] * (1 - sli_2) * (1 - fee_2)
        p3 = p_list[2] * (1 - sli_3) * (1 - fee_3)
        transaction, count = transaction_q(p1, p2, p3, q1, coin=coin, d_value=0)
        if coin == 'begin':
            q_list[0] += count
        elif coin == 'end':
            q_list[2] += count
        else:
            q_list[1] += count
    else:
        flag = 0
    return q_list, transaction, flag


def transaction_q(p1, p2, p3, q1, coin='end', d_value=1):
    """
    :param p1: htusdt 加上手续费的价格
    :param p2: hteth 加上手续费的价格
    :param p3: ethusdt 加上手续费的价格
    :param q1: 第一个币交易数量，已经进行百分比之后的币数
    :param coin: begin mid end ，分别代表三个币的位置 htusdt hteth ethusdt  ht-begin eth-mid usdt-end
    :param d_value: 1代表 p1-p2*p3>0  -1代表 p1-p2*p3<0
    :return: count 代表coin 的增加数量，transaction 代表 交易策略
    """
    transaction = []
    if coin == 'end':
        if d_value == 1:
            # sell htusdt
            transaction.append([-q1, q1 * p1])
            # buy hteth*ethusdt
            transaction.append([q1, -q1 * p2])
            transaction.append([q1 * p2, -q1 * p2 * p3])
            count = q1 * p1 - q1 * p2 * p3
        else:
            # buy htusdt
            transaction.append([q1, -q1 * p1])
            # sell  hteth*ethusdt
            transaction.append([-q1, q1 * p2])
            transaction.append([-q1 * p2, q1 * p2 * p3])
            count = - q1 * p1 + q1 * p2 * p3
    elif coin == 'begin':
        if d_value == 1:
            # sell htusdt
            transaction.append([-q1, q1 * p1])
            # buy hteth*ethusdt
            transaction.append([q1 * p1 / (p2 * p3), -q1 * p1 / p3])
            transaction.append([q1 * p1 / p3, -q1 * p1])
            count = q1 * p1 / (p2 * p3) - q1
        else:
            # buy htusdt
            transaction.append([q1, -q1 * p1])
            # sell  hteth*ethusdt
            transaction.append([-q1 * p1 / (p2 * p3), q1 * p1 / p3])
            transaction.append([-q1 * p1 / p3, q1 * p1])
            count = - q1 * p1 / (p2 * p3) + q1
    else:
        if d_value == 1:
            # sell htusdt
            transaction.append([-q1, q1 * p1])
            # buy hteth*ethusdt
            transaction.append([q1, -q1 * p2])
            transaction.append([q1 * p1 / p3, -q1 * p1])
            count = q1 * p1 / p3 - q1 * p2
        else:
            # buy htusdt
            transaction.append([q1, -q1 * p1])
            # sell  hteth*ethusdt
            transaction.append([-q1, q1 * p2])
            transaction.append([-q1 * p1 / p3, q1 * p1])
            count = - q1 * p1 / p3 + q1 * p2
    return transaction, count
