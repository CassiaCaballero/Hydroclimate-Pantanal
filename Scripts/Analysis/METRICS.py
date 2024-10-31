import numpy as np

def MAE(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))

def R2(y_true, y_pred):
    mean_y_true = np.mean(y_true)
    ss_total = np.sum((y_true - mean_y_true)**2)
    ss_residual = np.sum((y_true - y_pred)**2)
    r2 = 1 - (ss_residual / ss_total)
    return r2

def BIAS(y_true, y_pred):
    return np.mean(y_true - y_pred)

def RMSE(y_true, y_pred):
    mean_ = np.mean((y_pred - y_true) ** 2)
    rmse = np.sqrt(mean_)
    return (rmse)

def MAPE(y_true, y_pred):
    nonzero_indices = y_true != 0
    percentage_errors = np.abs((y_true[nonzero_indices] - y_pred[nonzero_indices]) / y_true[nonzero_indices])
    return np.mean(percentage_errors) * 100

def _maeLog_(y_true, y_pred):
    'Seegers (2018)'
    log_pMeasurement = np.log10(y_true)
    log_pEstimeted = np.log10(y_pred)
    # log_pMeasurement = [value for value in log_pMeasurement if not (math.isnan(value)) == True]
    # log_pEstimeted = [value for value in log_pEstimeted if not (math.isnan(value)) == True]
    mean_ = np.mean(abs(np.array(log_pEstimeted) - np.array(log_pMeasurement)))
    # mean_ = abs(np.array(log_pEstimeted) - np.array(log_pMeasurement))
    maeLog = 10 ** mean_
    return ( maeLog )

def _biasLog_(y_true, y_pred):
    'Seegers (2018)'
    log_pMeasurement = np.log10(y_true)
    log_pEstimeted = np.log10(y_pred)
    mean_ = np.mean(log_pEstimeted - log_pMeasurement)
    # mean_ = log_pEstimeted - log_pMeasurement
    biasLog = 10 ** mean_
    return ( biasLog )

def _mape_(y_true, y_pred):
    mape = (abs((y_pred - y_true) / y_true)) * 100
    mean = np.mean(mape)
    return mean

def _rmse_(y_true, y_pred):
    mean_ = np.mean((y_pred - y_true) ** 2)
    rmse = np.sqrt(mean_)
    return ( rmse )