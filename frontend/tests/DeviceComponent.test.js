import { render, screen } from '@testing-library/react';
import DeviceComponent from '../components/DeviceComponent';

test('renders devices header', () => {
  render(<DeviceComponent />);
  const headerElement = screen.getByText(/Devices/i);
  expect(headerElement).toBeInTheDocument();
});
