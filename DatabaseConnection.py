class Database:



    def connection_to_database(database_name='Practice', username='postgres', database_password='Dd3063489**'):
        import psycopg2 as pg2
        return (pg2.connect(database=database_name, user=username, password=database_password))

    def database_cursor(database_connection):
        return database_connection.cursor()

    def import_data_to_database(all_data_in_file, database_cursor, database_connection):
        for row in all_data_in_file:
            print((row))
            reference_id = row[0]
            trade_date = row[1]
            time_of_trade = row[2]
            underlying = row[3]
            expiration_date = row[4]
            strike_price = row[5]
            trade_type = row[6]
            open_interest = row[7]
            ind = row[8]
            ind = ind.upper()

            if ind == 'I':
                ind = 'AUTOX'
            elif ind == 'O':
                ind = 'CMBO'
            elif ind == 'S':
                ind = 'ISOI'
            elif ind == '':
                ind = 'REG'
            elif ind == 'M':
                ind = 'STDL'
            else:
                ind = 'BWRT'

            exchange_code = row[9]
            spread = row[10]
            premium_price = row[11]
            trade_size = row[12]
            bid_size = row[13]
            bid_price = row[14]
            ask_price = row[15]
            ask_size = row[16]
            edge = row[17]
            lean_size = row[18]
            size_ratio = row[19]
            trade_count = row[20]
            delta = row[21]
            theta = row[22]
            vega = row[23]
            gamma = row[24]
            sigma = row[25]
            rho = row[26]

            database_cursor.execute(f"""
                INSERT INTO master_trades(
                    reference_id,
                    trade_date,
                    time_of_trade,
                    underlying,
                    expiration_date,
                    strike_price,
                    trade_type,
                    open_interest,
                    ind,
                    exchange_code,
                    spread,
                    premium_price,
                    trade_size,
                    bid_size,
                    bid_price,
                    ask_price,
                    ask_size,
                    edge,
                    lean_size,
                    size_ratio,
                    trade_count,
                    delta,
                    theta,
                    vega, 
                    gamma, 
                    sigma, 
                    rho) 

                VALUES(
                    '{reference_id}', 
                    '{trade_date}',
                    '{time_of_trade}',
                    '{underlying}',
                    '{expiration_date}',
                    '{strike_price}',
                    '{trade_type}',
                    '{open_interest}',
                    '{ind}',
                    '{exchange_code}',
                    '{spread}',
                    '{premium_price}',
                    '{trade_size}',
                    '{bid_size}',
                    '{bid_price}',
                    '{ask_price}',
                    '{ask_size}',
                    '{edge}',
                    '{lean_size}',
                    '{size_ratio}',
                    '{trade_count}',
                    '{delta}',
                    '{theta}',
                    '{vega}',
                    '{gamma}',
                    '{sigma}',
                    '{rho}');""")

            database_connection.commit()

    def disconnect_database(database_connection):
        database_connection.close()
