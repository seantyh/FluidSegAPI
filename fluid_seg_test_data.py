def get_fluid_seg_test_data():    
    gran_label = ["0.33", "0.66", "1.00", "preseg", "token"]
    test_data = [
        ['今天來說的話', '，', '我想說', '，', '不知道大家要不要再研究看看', '。'],
        ['今天來說的話', '，', '我想說', '，', '不知道大家要不要', '再研究看看', '。'],
        ['今天來說', '的話', '，', '我想說', '，', '不知道', '大家', '要不要', '再研究', '看看', '。'],
        ['今天', '來說', '的話', '，', '我', '想', '說', '，', '不', '知道', 
            '大家', '要', '不', '要', '再', '研究', '看看', '。'],
        ['今', '天', '來', '說', '的', '話', '，', 
            '我', '想', '說', '，', '不', '知', '道', '大', '家', 
            '要', '不', '要', '再', '研', '究', '看', '看', '。'] 
    ]
    echo = '今天來說的話，我想說，不知道大家要不要再研究看看。'
    return {
        "granularity": gran_label, 
        "segments": test_data 
    }    