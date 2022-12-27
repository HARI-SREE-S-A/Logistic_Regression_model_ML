data = pd.read('file path')
features = data.drop('target column')
target =  data['target']

features_train,features_test,target_train,target_test = train_test_split(features,target,test_size = 0.20,stratify  = target,random_state  = 2)
