input_data  = ()
data_list = np.asarray(input_data)
reshaped_data = data_list.reshape(1,-1)

prediction_output = model.predict(reshaped_data)
