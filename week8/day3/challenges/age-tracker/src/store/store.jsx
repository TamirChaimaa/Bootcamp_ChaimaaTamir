import { configureStore } from '@reduxjs/toolkit';
import ageReducer from './ageSlice';

export const store = configureStore({
  reducer: {
    age: ageReducer,
  },
});
