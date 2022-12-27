//training accuracy


train_pred = model.predict(features.train)
training_accuracy = accuracy_score(train_pred,target_train)



//Testing accuracy


test_pred = model.predict(features_test)
testing_accuracy = accuracy_score(test_pred,target_test)
