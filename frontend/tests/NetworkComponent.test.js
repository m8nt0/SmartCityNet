import { render, screen } from '@testing-library/react';
import NetworkComponent from '../components/NetworkComponent';

test('renders networks header', () => {
  render(<NetworkComponent />);
  const headerElement = screen.getByText(/Networks/i);
  expect(headerElement).toBeInTheDocument();
});
