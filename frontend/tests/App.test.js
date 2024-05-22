import { render, screen } from '@testing-library/react';
import App from '../components/App';

test('renders devices link', () => {
  render(<App />);
  const linkElement = screen.getByText(/Devices/i);
  expect(linkElement).toBeInTheDocument();
});
