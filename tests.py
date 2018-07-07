from fynd import Fynd as fynd

COLLECTION = {
    'blogposts': [
        {
            'title': 'Lorem Ipsum',
            'text': 'Dolor Sit Amet Blah Blah Blah'
        },
        {
            'title': 'Brown Fox',
            'text': 'The quick brown fox jumps over blah'
        }
    ]
}

def test_default_case():
    result_a = fynd('blah').inside(COLLECTION)
    result_b = fynd('lorem').inside(COLLECTION)
    assert (
        result_a == [['blogposts', 0, 'text'], ['blogposts', 1, 'text']]
        and result_b == [['blogposts', 0, 'title']]
    )

def test_case_sensitive_case():
    result_a = fynd('Blah').case_sensitive().inside(COLLECTION)
    result_b = fynd('blah').case_sensitive().inside(COLLECTION)
    assert (
        result_a == [['blogposts', 0, 'text']]
        and result_b == [['blogposts', 1, 'text']]
    )

def test_not_found_case():
    result_a = fynd('hulalala').inside(COLLECTION)
    result_b = fynd('').inside(COLLECTION)
    assert (
        result_a == []
        and result_b == []
    )

def test_collection_integrity():
    result_a = fynd('blah').inside(COLLECTION)
    result_b = fynd('lorem').inside(COLLECTION)
    result_c = fynd('Fox').inside(COLLECTION)
    result_d = fynd('Fox').case_sensitive().inside(COLLECTION)
    assert (
        result_a == [['blogposts', 0, 'text'], ['blogposts', 1, 'text']]
        and result_b == [['blogposts', 0, 'title']]
        and result_c == [['blogposts', 1, 'title'], ['blogposts', 1, 'text']]
        and result_d == [['blogposts', 1, 'title']]
        and COLLECTION['blogposts'][0]['title'] == 'Lorem Ipsum'
        and COLLECTION['blogposts'][0]['text'] == 'Dolor Sit Amet Blah Blah Blah'
        and COLLECTION['blogposts'][1]['title'] == 'Brown Fox'
        and COLLECTION['blogposts'][1]['text'] == 'The quick brown fox jumps over blah'
    )

def main():
    result = fynd('blah').inside(COLLECTION)
    print("Searched For 'blah': \n", result)
    result = fynd('lorem').inside(COLLECTION)
    print("Searched For 'lorem': \n", result)
    result = fynd('Blah').case_sensitive().inside(COLLECTION)
    print("Searched For 'Blah' Case Sensitive: \n", result)
    result = fynd('blah').case_sensitive().inside(COLLECTION)
    print("Searched For 'blah' Case Sensitive: \n", result)
    result = fynd('hulalala').inside(COLLECTION)
    print("Searched For 'hulalala': \n", result)
    result = fynd('').inside(COLLECTION)
    print("Searched For '': \n", result)

if __name__ == '__main__':
    main()
