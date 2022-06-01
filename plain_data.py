def plain_data(data: list):
    """
    This function takes an n dimension list and it flattens it to 1 dimension
    :return: Returns flat list
    """
    if not isinstance(data, list):  # Here we are making sure that we are passing a list
        return 'type error'
    if len(data) == 0:  # Here we check if the list is empty
        return data
    if isinstance(data[0], list):  # Here we check if the instance is another list
        # If it is we use recursion to see if there is another list inside that element. We do this until the list is completely flat
        return plain_data(data[0]) + plain_data(data[1:])
    return data[:1] + plain_data(data[1:])  # Here we use recursion again until we don't have anymore nested lists and we return the flat list

