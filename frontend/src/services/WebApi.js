import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
export const api = createApi({
  reducerPath: "api",
  baseQuery: fetchBaseQuery({ baseUrl: "http://localhost:8000" }),
  endpoints: (builder) => ({
    getServices: builder.query({
      query: () => "services",
    }),
  }),
});
const fetchServices = createAsyncThunk("services/fetchServices", async () => {
  const response = await api.endpoints.getServices();
  return response.data;
});
const servicesSlice = createSlice({
  name: "services",
  initialState: {
    services: [],
    status: "idle",
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchServices.pending, (state) => {
        state.status = "loading";
      })
      .addCase(fetchServices.fulfilled, (state, action) => {
        state.status = "succeeded";
        state.services = action.payload;
      })
      .addCase(fetchServices.rejected, (state, action) => {
        state.status = "failed";
        state.error = action.error.message;
      });
  },
});
export const { reducer } = servicesSlice;
export const { useGetServicesQuery } = api;
export { fetchServices };