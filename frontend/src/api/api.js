// Placeholder for API-related functions or configurations

/**
 * The fetchData function simulates an API call to retrieve chart and table data.
 * It returns a hardcoded response containing sample data for demonstration purposes.
 *
 * @returns {Promise<Object>} A promise that resolves to an object containing
 *                            sample chartData and tableData.
 *                            chartData: Array of numbers representing data for a chart.
 *                            tableData: Array of objects representing rows for a table,
 *                                       each with an id, name, and value.
 */
export const fetchData = async () => {
    return {
        // Sample data for a chart visualization
        chartData: [10, 20, 30],
        // Sample data for a table display
        tableData: [
            { id: 1, name: 'Item 1', value: 100 },
            { id: 2, name: 'Item 2', value: 200 }
        ]
    };
};