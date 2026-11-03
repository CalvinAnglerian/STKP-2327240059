import xmlrpc.client

APPLICATION_URL = "http://application:8000/"


def check_in(passenger_id, passenger_name, flight_code):

    with xmlrpc.client.ServerProxy(
        APPLICATION_URL,
        allow_none=True
    ) as server:

        result = server.process_check_in(
            passenger_id,
            passenger_name,
            flight_code
        )

        return result


def get_stats():

    with xmlrpc.client.ServerProxy(
        APPLICATION_URL,
        allow_none=True
    ) as server:

        return server.get_database_stats()


def get_all_checkins():

    with xmlrpc.client.ServerProxy(
        APPLICATION_URL,
        allow_none=True
    ) as server:

        return server.get_all_checkins()