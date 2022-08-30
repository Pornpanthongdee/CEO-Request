import os
import pandas as pd


class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Hints 1: Build csv_path as "absolute path" in order to call this method from anywhere.
            # Do not hardcode your path as it only works on your machine ('Users/username/code...')
            # Use __file__ instead as an absolute path anchor independant of your usename
            # Make extensive use of `breakpoint()` to investigate what `__file__` variable is really
        # Hint 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities
        root_dir = os.path.dirname(os.path.dirname(__file__))
        csv_path = os.path.join(root_dir, "data", "csv")
        file_names = [f for f in os.listdir(csv_path) if f.endswith('.csv')]
        key_names = [key_name
            .replace('olist_','')
            .replace('_dataset','')
            .replace('.csv','')
            for key_name in file_names]
        data = {}
        for k,f in zip(key_names, file_names):
            data[k] = pd.read_csv(os.path.join(csv_path, f))
        return data

    def get_matching_table(self):
        """
        01-01 > This function returns a matching table between
        columns [ "order_id", "review_id", "customer_id", "product_id", "seller_id"]
        """
        # Get data
        data = self.get_data()
        # Filter only on order_status delivered
        orders = data['orders']
        orders = orders[orders['order_status']=='delivered']
        reviews = data['order_reviews']
        order_items = data['order_items']
        # Select only the columns of interest
        orders = orders[['order_id', 'customer_id']]
        reviews = reviews[['review_id', 'order_id']]
        order_items = order_items[['order_id', 'product_id', 'seller_id']]
        # Merge DataFrame
        merge_df = orders.merge(reviews, on='order_id', how='outer').merge(order_items, on='order_id', how='outer')

        return merge_df

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
