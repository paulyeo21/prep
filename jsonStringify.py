# JSON stringify method converts an object or value to a JSON string.

# Clarifications:
#   a) Given an object or value convert to a valid JSON string format. Valid JSON
#      format involves data in name/value pairs, data separated by commas, curly
#      braces to hold objects, and square brackets to hold arrays. Can be hash or array 
#      with nested hashes or arrays like {key:{key1:{}} or of the like ['here', True, None].
#   b) Break it down into valid syntax which are (name/value pairs, commas, curly braces, square
#      brackets) and valid values (string, number, object, array, boolean, null).
#   c) Given {'x': 5, 'y': 6} return "{'x':5,'y':6}"
#   d) Given [new Thing('thing'), True, None] return "['thing',True,None]"
#
# Edge cases:
#   a) Given None return None
#   b) Given invalid JSON such as 'string' raise Exception
#   c) Given {} return '{}'
#   d) Given [] return '[]'
#
# Algorithms:
#   a) if array iterate over each element and concatenate the string representation
#      to the output string.
#   b) if key/value, such as {key: {key1: [value1, value2], key2: value3}}, then you should
#      concatenate key to output string, then repeat process for value. For instance, add
#      key to output string and call the same function on the value to key. 

def jsonStringifyObjectHelper(json, syntax):
    if isinstance(json, str):
        return syntax + json + syntax
    else:
        return str(json)

def jsonStringifyArrayHelper(json, syntax):
    output = '['
    for i in range(len(json)):
        output += jsonStringifyObjectHelper(json[i], syntax)
        if not len(json)-1 == i:
            output += ','
    return output + ']'

def jsonStringifyDictHelper(json, syntax):
    output = '{'
    for key, value in json.iteritems():
        output += syntax + key + syntax + ':'
        output += jsonStringifyCollectionHelper(value)
        output += ','
    return output + '}'

def jsonStringifyCollectionHelper(json):
    output = ''
    if output == '':
        syntax = '"'
    else:
        syntax = "'"

    if isinstance(json, list):
        return jsonStringifyArrayHelper(json, syntax)
    elif isinstance(json, dict):
        return jsonStringifyDictHelper(json, syntax)
    else:
        return output + jsonStringifyObjectHelper(json, '"')

def jsonStringify(json):
    if json == None:
        return None
    if not isinstance(json, list) and not isinstance(json, dict):
        raise Exception('invalid JSON input')
    return jsonStringifyCollectionHelper(json)

assert(jsonStringify(None) == None)
assert(jsonStringify([]) == '[]')
assert(jsonStringify([True, False, 'string']) == '[True,False,"string"]')
assert(jsonStringify({}) == '{}')
print(jsonStringify({'key1': 'value1', 'key2': 'value2'}))
# assert(jsonStringify({'key1': 'value1', 'key2': 'value2'}) == '{"key1":"value1","key2":"value2"}')
jsonStringify('string') # expect Exception
