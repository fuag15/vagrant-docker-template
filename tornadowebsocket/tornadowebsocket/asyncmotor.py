"""
Async helpers for Motor client
"""

async def find_one(database, 
                   query, 
                   success_callback,
                   error_callback):
    """
    Asynchronous database call back
    to fetch an object from mongo
    and pass results to a callback
    
    :param database:
        a database handle to the desired
        database and collection to query
    :type database:
        :class:`MotorCollection`
    
    :param query:
        a database query to make
        against the collection
    :type query:
        any valid mongo query

    :param success_callback:
        function that takes one parameter
        and does something with it. That parameter
        will be None or the mongo object
    :type success_callback:
        :class:`Callable`

    :param error_callback:
        function that takes one parameter
        and does something with it. That parameter
        will be any exceptions raised
    :type error_callback
        :class:`Callable`
    """
    try:
        success_callback(await database.find_one(query))
    except Exception as motor_error:
        error_callback(motor_error)

async def insert(database, 
                 data,
                 success_callback,
                 error_callback):
    """
    Asynchronous database call back
    to insert an object to mongo
    
    :param database:
        a database handle to the desired
        database and collection to query
    :type database:
        :class:`MotorCollection`
    
    :param data:
        data to insert to the db
    :type data:
        any valid data to insert to mongo

    :param success_callback:
        function that takes one parameter
        and does something with it. That parameter
        will be None or the mongo object
    :type success_callback:
        :class:`Callable`

    :param error_callback:
        function that takes one parameter
        and does something with it. That parameter
        will be any exceptions raised
    :type error_callback
        :class:`Callable`
    """
    try:
        success_callback(await database.insert(data))
    except Exception as motor_error:
        error_callback(motor_error)
